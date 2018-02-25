from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
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
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question,
    }
    return render(request, 'polls/detail.html', context)
    """
    # when `get_object_or_404` is not used
    try:
        question = Question.objects.get(pk=question_id)
        context = {
            'question': question,
        }
    except Question.DoesNotExist:
        raise Http404('Question %s does not exist.' % question_id)
    return render(request, 'polls/detail.html', context)
    """


def results(request, question_id):
    response = '[results] question_id = %s'
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse('[vote] question_id = %s' % question_id)
