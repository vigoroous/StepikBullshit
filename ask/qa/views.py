from django.http import HttpResponse
from django.shortcuts import render
from django.http.response import Http404
from django.core.paginator import Paginator
from .models import Answer, Question
from .forms import AskForm, AnswerForm


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def home(request):
    try:
        limit = int(request.GET.get('limit', 10))
    except:
        limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except:
        page = 1
    paginator = Paginator(Question.objects.new(), limit)
    articles = paginator.page(page)
    return render(request, 'qa/recent_questions.html', {'articles': articles})


def popular(request):
    try:
        limit = int(request.GET.get('limit', 10))
    except:
        limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except:
        page = 1
    paginator = Paginator(Question.objects.popular(), limit)
    articles = paginator.page(page)
    return render(request, 'qa/popular_questions.html', {'articles': articles})


def question(request, id):
    try:
        this_question = Question.objects.get(pk=id)
        answers = Answer.objects.all().filter(question=id)
        err_message = ''

        if request.method == "POST":
            answer_form = AnswerForm(request.POST)
            if answer_form.is_valid():
                created_answer = answer_form.save()
                resp = HttpResponse(content='', status=302)
                resp['Location'] = '/question/' + str(created_answer.question.id)
                return resp
            else:
                err_message = 'Invalid form data'
        else:
            answer_form = AnswerForm(initial={'question': id})

        data = {
            'question': this_question,
            'answers': answers,
            'form': answer_form,
        }
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'qa/question_details.html', data)


def ask(request):
    err_message = ''
    if request.method == "POST":
        ask_form = AskForm(request.POST)
        if ask_form.is_valid():
            created_question = ask_form.save()
            resp = HttpResponse(content='', status=302)
            resp['Location'] = '/question/' + str(created_question.id)
            return resp
        else:
            err_message = 'Invalid form data'
    else:
        ask_form = AskForm()

    data = {
        'form': ask_form,
        'error': err_message,
    }
    return render(request, 'qa/ask.html', data)
