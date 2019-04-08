from django.shortcuts import render
from django.utils import timezone
from django.views.generic import TemplateView
from .models import Question

Danil = ({'photo': 'images/Danil.jpg'})
MiSa = ({'photo': 'images/MiSa.jpg'})
Anton = ({'photo': 'images/Anton.jpg'})

tags = []
tags.append({'text': "linear-algebra"})
tags.append({'text': "matrices"})
tags.append({'text': "permutations"})
tags.append({'text': "combinatorics"})
tags.append({'text': "calculus"})
tags.append({'text': "real-analysis"})
tags.append({'text': "integration"})

questions = []
for i in range(1, 11):
    questions.append({
        'id': 3 * (i - 1) + 1,
        'title': "Linear algebra objective type question",
        'content': "Let M be an n×n hermition matrix of rank k if λ≠0 be an eigen value of M with corresponding unit column vector as eigen vector u i.e. Mu=λu. Then we must have...",
        'tags': tags[0:2],
        'author': MiSa,
        'rate': 3 * (i - 1) + 1
    })
    questions.append({
        'id': 3 * (i - 1) + 2,
        'title': "Number of five digit numbers that can be formed with this condition",
        'content': "How many five digit numbers can be made having the digits 1,2,3 each of which can be used at most thrice in a number?",
        'tags': tags[2:5],
        'author': Danil,
        'rate': 3 * (i - 1) + 2
    })
    questions.append({
        'id': 3 * (i - 1) + 3,
        'title': "Difference between Riemann sums and Riemann integrals",
        'content': "Let M be an n×n hermition matrix of rank k if λ≠0 be an eigen value of M with corresponding unit column vector as eigen vector u i.e. Mu=λu. Then we must have...",
        'tags': tags[5:7],
        'author': Anton,
        'rate': 3 * (i - 1) + 3
    })


def question_list(request):
    # questions = Question.objects.all()
    return render(request, 'questions/index.html', {'questions': questions})

    # return render(request, 'questions/index.html', {})


def base(request):
    return render(request, 'questions/base.html', {})


def question(request):
    return render(request, 'questions/question.html', {})


def ask(request):
    return render(request, 'questions/ask.html', {})


def login(request):
    return render(request, 'questions/login.html', {})


def signup(request):
    return render(request, 'questions/signup.html', {})


def settings(request):
    return render(request, 'questions/settings.html', {})

# class AboutView(TemplateView):
#     template_name = "questions/base.html"


