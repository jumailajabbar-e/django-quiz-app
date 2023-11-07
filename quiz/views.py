
from django.shortcuts import render, redirect
from .models import Question, Choice

def custom_quiz_view(request):
    if request.method == 'POST':
    
        score = 0
        for question in Question.objects.all():
            selected_option_id = request.POST.get(f'question_{question.id}')
            correct_option = question.option_set.filter(is_correct=True).first()
            if selected_option_id and selected_option_id == str(correct_option.id):
                score += 1

        return render(request, 'quiz/quiz_result.html', {'score': score})
    else:
        
        questions = Question.objects.all()
        context = {'questions': questions}
        return render(request, 'quiz/custom_quiz.html', context)
