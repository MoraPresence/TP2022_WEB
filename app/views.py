from django.shortcuts import render, get_object_or_404

from CatOverflow.paginator import paginate

# @require_GET
from .models import Question, Answer, get_best_members, get_popular_tags


def index(request):
    page_list = Question.objects.new_questions()
    context = paginate(page_list, request, 4)

    return render(request, 'index.html',
                  {'questions': context, 'best_members': get_best_members(), 'popular_tags': get_popular_tags()})


def question(request, question_id: int):
    question_item = get_object_or_404(Question, pk=question_id)
    context = paginate(Answer.objects.filter(question_id=question_id), request, 4)
    return render(request, 'question.html',
                  {'question': question_item, 'answers': context, 'best_members': get_best_members(),
                   'popular_tags': get_popular_tags()})


def ask(request):
    return render(request, 'ask.html', {'best_members': get_best_members(), 'popular_tags': get_popular_tags()})


def login(request):
    return render(request, 'login.html', {'best_members': get_best_members(), 'popular_tags': get_popular_tags()})


def register(request):
    return render(request, 'register.html', {'best_members': get_best_members(), 'popular_tags': get_popular_tags()})


def settings(request):
    return render(request, 'settings.html', {'best_members': get_best_members(), 'popular_tags': get_popular_tags()})


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
