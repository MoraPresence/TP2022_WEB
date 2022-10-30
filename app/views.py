import string

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_GET


# @require_GET
def index(request):
    return render(request, 'index.html')


def question(request, question_id: int):
    return render(request, 'question.html')


def ask(request):
    return render(request, 'ask.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def settings(request):
    return render(request, 'settings.html')


def tag(request, tag):
    return render(request, 'tag.html')

