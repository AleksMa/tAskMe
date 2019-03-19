from django.shortcuts import render
from django.views.generic import TemplateView

def question_list(request):
    return render(request, 'questions/index.html', {})

def base(request):
    return render(request, 'questions/base.html', {})


# class AboutView(TemplateView):
#     template_name = "questions/base.html"


QUESTIONS = {

}