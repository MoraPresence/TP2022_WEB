from django.contrib import auth
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from CatOverflow.paginator import paginate

# @require_GET
from .forms import LoginForm, RegisterForm, SettingsForm, QuestionForm, AnswerForm
from .models import Question, Answer, get_best_members, get_popular_tags


def index(request):
    page_list = Question.objects.new_questions()
    context = paginate(page_list, request, 4)

    return render(request, 'index.html',
                  {'questions': context, 'best_members': get_best_members(), 'popular_tags': get_popular_tags()})


def question(request, question_id: int):
    initial_data = {'question': question_id, 'author': request.user.profile}
    answer_form = {}

    if request.method == "GET":
        answer_form = AnswerForm(initial=initial_data)

    if request.method == 'POST':
        if request.user.is_authenticated:
            answer_form = AnswerForm(initial=initial_data, data=request.POST)
            if answer_form.is_valid():
                answer = answer_form.save()
                if answer:
                    return redirect(reverse('index'))
                else:
                    answer_form.add_error(field=None, error="Answer saving error")
        else:
            answer_form.add_error(field=None, error="You not authenticated")

    question_item = get_object_or_404(Question.objects.questions(), pk=question_id)
    context = paginate(Answer.objects.hot_answers().filter(question_id=question_id), request, 4)

    return render(request, 'question.html',
                  {'form': answer_form, 'question': question_item, 'answers': context,
                   'best_members': get_best_members(),
                   'popular_tags': get_popular_tags()})


@require_http_methods(['GET', 'POST'])
def ask(request):
    if request.method == "GET":
        question_form = QuestionForm()

    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        if question_form.is_valid():
            user = question_form.save()
            if user:
                return redirect(reverse('login'))
            else:
                question_form.add_error(field=None, error="User saving error")
    return render(request, 'ask.html',
                  {'form': question_form, 'best_members': get_best_members(), 'popular_tags': get_popular_tags()})


@require_http_methods(['GET', 'POST'])
def login(request):
    if request.method == "GET":
        user_form = LoginForm()

    if request.method == 'POST':
        user_form = LoginForm(request.POST)
        if user_form.is_valid():
            user = auth.authenticate(request=request, **user_form.cleaned_data)
            if user:
                auth.login(request, user)
                return redirect(reverse('index'))
            else:
                user_form.add_error(field=None, error="Wrong username or password")
    return render(request, 'login.html',
                  {'form': user_form, 'best_members': get_best_members(), 'popular_tags': get_popular_tags()})


@require_http_methods(['GET', 'POST'])
def register(request):
    if request.method == "GET":
        user_form = RegisterForm()

    if request.method == 'POST':
        user_form = RegisterForm(request.POST, request.FILES)
        if user_form.is_valid():
            user = user_form.save()
            if user:
                return redirect(reverse('login'))
            else:
                user_form.add_error(field=None, error="User saving error")
    return render(request, 'register.html',
                  {'form': user_form, 'best_members': get_best_members(), 'popular_tags': get_popular_tags()})


@login_required(login_url="login", redirect_field_name="continue")
@require_http_methods(['GET', 'POST'])
def settings(request):
    if request.method == "GET":
        initial_data = model_to_dict(request.user)
        user_form = SettingsForm(initial=initial_data)

    if request.method == 'POST':
        user_form = SettingsForm(request.POST, request.FILES, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect(reverse('index'))
        else:
            user_form.add_error(field=None, error="Invalid POST data")

    return render(request, 'settings.html',
                  {'form': user_form, 'best_members': get_best_members(), 'popular_tags': get_popular_tags()})


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


@login_required
def logout_view(request):
    auth.logout(request)
    return redirect(reverse('index'))
