from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:page_num>/', views.index, name='index'),
    path('base', views.base, name='base'),
    path('question/<question_id>', views.question, name='question'),
    path('tag/<tag_name>', views.tag, name='tag'),
    path('ask', views.ask, name='ask'),
    path('signup', views.signup, name='signup'),
    path('settings', views.settings, name='settings'),
]
