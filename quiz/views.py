from django.shortcuts import render, redirect
from .models import Question

def home(request):
    return render(request, 'quiz/home.html')

def start_quiz(request):
    questions = Question.objects.order_by('?')[:20]

    request.session['questions'] = list(questions.values_list('id', flat=True))
    request.session['current'] = 0
    request.session['score'] = 0
    request.session['answers'] = {}  # 🆕

    return redirect('quiz_question')


def quiz_question(request):
    questions_ids = request.session.get('questions', [])
    current = request.session.get('current', 0)

    # 🏁 fin du quiz
    if current >= len(questions_ids):
        return redirect('quiz_result')

    question = Question.objects.get(id=questions_ids[current])

    if request.method == 'POST':
        selected = request.POST.get('answer')

        # 📦 sauvegarde réponse
        answers = request.session.get('answers', {})
        answers[str(question.id)] = selected
        request.session['answers'] = answers

        if selected == question.correct_answer:
            request.session['score'] += 1

        request.session['current'] += 1
        return redirect('quiz_question')

    return render(request, 'quiz/question.html', {
        'question': question,
        'number': current + 1,
        'total': len(questions_ids)
    })


def quiz_result(request):
    questions_ids = request.session.get('questions', [])
    answers = request.session.get('answers', {})

    questions = Question.objects.filter(id__in=questions_ids)

    results = []

    for q in questions:
        user_answer = answers.get(str(q.id))

        results.append({
            'question': q.text,
            'correct': q.correct_answer,
            'user': user_answer,
            'is_correct': user_answer == q.correct_answer
        })

    return render(request, 'quiz/result.html', {
        'score': request.session.get('score', 0),
        'total': len(questions_ids),
        'results': results
    })