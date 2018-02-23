# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('Hello, polls.')


def detail(request, question_id):
    return HttpResponse('[detail] question_id = %s' % question_id)


def results(request, question_id):
    response = '[results] question_id = %s'
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse('[vote] question_id = %s' % question_id)
