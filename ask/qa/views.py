from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render
from django.http.response import Http404
from django.core.paginator import Paginator
from .models import Answer, Question
from .forms import AskForm, AnswerForm, SignupForm, LoginForm


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
            # immutable structure
            init_form = request.POST.copy()
            init_form['question'] = id
            init_form['author'] = request.user
            answer_form = AnswerForm(init_form)
            if answer_form.is_valid():
                created_answer = answer_form.save()
                resp = HttpResponse(content='', status=302)
                resp['Location'] = '/question/' + str(created_answer.question.id)
                return resp
            else:
                err_message = 'Invalid form data'
        else:
            answer_form = AnswerForm()            
        data = {
            'question': this_question,
            'answers': answers,
            'form': answer_form,
            'error': err_message,
        }
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'qa/question_details.html', data)


def ask(request):
    err_message = ''
    if request.method == "POST":
        init_form = request.POST.copy()
        init_form['author'] = request.user
        ask_form = AskForm(init_form)
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


def signup_view(request):
    err_message = ''
    if request.method == "POST":
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            resp = HttpResponse(content='', status=302)
            resp['Location'] = '/login/'
            return resp
        else:
            err_message = 'Invalid form data'
    else:
        signup_form = SignupForm()
    data = {
        'form': signup_form,
        'error': err_message,
    }
    return render(request, 'qa/signup.html', data)


def login_view(request):
    err_message = ''

    if request.method == "POST":
        login_form = LoginForm(request, request.POST)
        if login_form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                resp = HttpResponse(content='', status=302)
                resp['Location'] = '/'
                return resp
            else:
                err_message = "Invalid login credentials"            
        else:
            err_message = 'Invalid form data'
    else:
        login_form = LoginForm()
    data = {
        'form': login_form,
        'error': err_message,
    }
    return render(request, 'qa/login.html', data)

def logout_view(request):
    logout(request)
    resp = HttpResponse(content='', status=302)
    resp['Location'] = '/'
    return resp
    # Redirect to a success page.