from django.urls import path
from . import views

urlpatterns = [
    path('', views.question_list, name='index'),
    path('base', views.base, name='base'),
]
