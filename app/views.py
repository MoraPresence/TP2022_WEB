from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_GET


# @require_GET 33:30
def index(request):
    return HttpResponse("Hello, world!")
