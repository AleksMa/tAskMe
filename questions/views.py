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

answers = []
for i in range(1, 3):
    answers.append({
        'id': i,
        'content': '''Unfortunately, you're making distinctions where there aren't any--for example, one digit 1 is the same as any other, 
        though it may have a different meaning once we choose a place for it. 
        The first thing I notice about this problem is that, if I want to directly count the desired numbers, 
        there will be several cases and subcases. We could start with the case of no 1s 
        with subcases two 2s and three 2s), then the case of a single 1 (with subcases one 2, two 2s, and three 2s), 
        and so on. That seems like a pain, though.''',
        'author': MiSa,
        'rate': i
    })


def question_list(request):
    # questions = Question.objects.all()
    return render(request, 'questions/index.html', {'questions': questions})

    # return render(request, 'questions/index.html', {})


def base(request):
    return render(request, 'questions/base.html', {})


def question(request, question_id):
    return render(request, 'questions/question.html', {'answers': answers, 'question': questions[int(question_id)-1]})


def tag(request, tag_name):
    tag_obj = {'text': tag_name}

    def is_tag(q):
        return tag_obj in q['tags']

    qs = filter(is_tag, questions)
    return render(request, 'questions/tag.html', {'tag': tag_name, 'questions': qs})


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
