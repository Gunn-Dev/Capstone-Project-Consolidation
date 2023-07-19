from django.shortcuts import render
from .models import Question

def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_questions': latest_questions}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = Question.objects.get(pk=question_id)
    context = {'question': question}
    return render(request, 'polls/detail.html', context)

def vote(request, question_id):
    question = Question.objects.get(pk=question_id)
    # Voting logic here
    return render(request, 'polls/vote.html', context)
