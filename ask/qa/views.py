from django.http import HttpResponse
from django.shortcuts import render
from django.http.response import Http404
from .models import Question, QuestionManager


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def home(request):
    pass


def popular(request):
    pass


def question(request, id):
    try:
        question = Question.objects.get(pk = id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'qa/question.html', {'question': question})
    # question = Question.objects.all()
    # return HttpResponse(question)