from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.http import require_GET
from django.views.generic import ListView

from CatOverflow.paginator import paginate
from . import models
from CatOverflow import paginator


# @require_GET
def index(request):
    page_list = models.QUESTIONS
    return render(request, 'index.html', paginate(page_list, request, 4))


def question(request, question_id: int):
    question_item = models.QUESTIONS[question_id]
    context = paginate(models.ANSWERS, request, 2)
    return render(request, 'question.html', {'question': question_item, 'comments': context})


def ask(request):
    return render(request, 'ask.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def settings(request):
    return render(request, 'settings.html')


def tag(request, tag_id):
    tag_list = models.QUESTIONS
    return render(request, 'tag.html', paginate(tag_list, request))
