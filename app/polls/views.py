from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader

# Create your views here.


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list
    }
    return HttpResponse(template.render(context, request))

def index_by_render(request):
    """`index` method by `django.shortcuts.render`
    """
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    return HttpResponse('[detail] question_id = %s' % question_id)


def results(request, question_id):
    response = '[results] question_id = %s'
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse('[vote] question_id = %s' % question_id)
