from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_GET
from . import models


# @require_GET
def index(request):
    question_list = {'questions': models.QUESTIONS}
    return render(request, 'index.html', context=question_list)


def question(request, question_id: int):
    question_item = models.QUESTIONS[question_id]
    answer_list = {'answers': models.ANSWERS}
    return render(request, 'question.html', {'question' : question_item, 'answers': models.ANSWERS})


def ask(request):
    return render(request, 'ask.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def settings(request):
    return render(request, 'settings.html')


def tag(request, tag_id):
    tag_list = {'questions': models.QUESTIONS}
    return render(request, 'tag.html', context=tag_list)
