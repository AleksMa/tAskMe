from django.urls import path
from . import views

urlpatterns = [
    path('', views.question_list, name='index'),
    path('base', views.base, name='base'),
    path('question', views.question, name='question'),
    path('ask', views.ask, name='ask'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('settings', views.settings, name='settings'),
]
