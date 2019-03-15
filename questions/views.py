from django.shortcuts import render

def question_list(request):
    return render(request, 'questions/base.html', {})