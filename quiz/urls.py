from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # 🏠 accueil
    path('start/', views.start_quiz, name='start_quiz'),
    path('question/', views.quiz_question, name='quiz_question'),
    path('result/', views.quiz_result, name='quiz_result'),
]