from django.contrib import auth
from django.contrib.auth import logout
from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from CatOverflow.paginator import paginate

# @require_GET
from .forms import LoginForm, RegisterForm, SettingsForm
from .models import Question, Answer, get_best_members, get_popular_tags


def index(request):
    page_list = Question.objects.new_questions()
    context = paginate(page_list, request, 4)

    return render(request, 'index.html',
                  {'questions': context, 'best_members': get_best_members(), 'popular_tags': get_popular_tags()})


def question(request, question_id: int):
    question_item = get_object_or_404(Question.objects.questions(), pk=question_id)
    context = paginate(Answer.objects.hot_answers().filter(question_id=question_id), request, 4)
    return render(request, 'question.html',
                  {'question': question_item, 'answers': context, 'best_members': get_best_members(),
                   'popular_tags': get_popular_tags()})


def ask(request):
    return render(request, 'ask.html', {'best_members': get_best_members(), 'popular_tags': get_popular_tags()})


def login(request):
    if request.method == "GET":
        user_form = LoginForm()

    if request.method == 'POST':
        user_form = LoginForm(request.POST)
        if user_form.is_valid():
            user = auth.authenticate(request=request, **user_form.cleaned_data)
            if user:
                return redirect(reverse('index'))
            else:
                user_form.add_error(field=None, error="Wrong username or password")
    return render(request, 'login.html',
                  {'form': user_form, 'best_members': get_best_members(), 'popular_tags': get_popular_tags()})


def register(request):
    if request.method == "GET":
        user_form = RegisterForm()

    if request.method == 'POST':
        user_form = RegisterForm(request.POST, request.FILES)
        if user_form.is_valid():
            user = user_form.save()
            if user:
                return redirect(reverse('index'))
            else:
                user_form.add_error(field=None, error="User saving error")
    return render(request, 'register.html',
                  {'form': user_form, 'best_members': get_best_members(), 'popular_tags': get_popular_tags()})


@require_http_methods(['GET', 'POST'])
def settings(request):
    if request.method == "GET":
        initial_data = model_to_dict(request.user)
        user_form = SettingsForm(initial=initial_data)

    if request.method == 'POST':
        initial_data = {}
        user_form = {}
    return render(request, 'settings.html', {'form': user_form, 'best_members': get_best_members(), 'popular_tags': get_popular_tags()})


def tag(request, tag_id):
    tag_list = Question.objects.tag_questions(tag_id)
    context = paginate(tag_list, request, 4)
    return render(request, 'tag.html',
                  {'questions': context, 'best_members': get_best_members(), 'popular_tags': get_popular_tags()})


def hot(request):
    page_list = Question.objects.hot_questions()
    context = paginate(page_list, request, 4)

    return render(request, 'index.html',
                  {'questions': context, 'best_members': get_best_members(),
                   'popular_tags': get_popular_tags()})


def logout_view(request):
    auth.logout(request)
    return redirect(reverse('index'))
