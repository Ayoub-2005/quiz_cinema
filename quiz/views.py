import random
from .models import Question
from django.shortcuts import render

def index(request):
    return render(request, 'quiz/index.html')


def quiz(request):

    all_questions = list(Question.objects.all())

    # ⚠️ sécurité si moins de 20 questions
    if len(all_questions) < 20:
        questions = all_questions
    else:
        questions = random.sample(all_questions, 20)

    request.session['questions'] = [q.id for q in questions]

    if request.method == "POST":
        score = 0
        selected_ids = request.session.get('questions', [])
        questions = Question.objects.filter(id__in=selected_ids)

        for q in questions:
            user_answer = request.POST.get(str(q.id))
            if user_answer == q.answer:
                score += 1

        return render(request, 'quiz/result.html', {
            "score": score,
            "total": len(questions)
        })

    return render(request, 'quiz/quiz.html', {"questions": questions})