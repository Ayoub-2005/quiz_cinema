from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='quiz_index'),
    path('quiz/', views.quiz, name='quiz'),
]