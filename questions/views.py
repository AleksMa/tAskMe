from django.shortcuts import render
from django.views.generic import TemplateView

def question_list(request):
    return render(request, 'questions/index.html', {})

def base(request):
    return render(request, 'questions/base.html', {})

def question(request):
    return render(request, 'questions/quest.html', {})

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


QUESTIONS = {

}