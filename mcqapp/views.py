from django.shortcuts import render,HttpResponse
# from .models import Quiz
from mcqapp.models import Quiz


# Create your views here.

def index(request):
    # quizs = Quiz.objects.filter(is_published= True).order_by('-list_date')

    quizs = Quiz.objects.order_by('-list_date').filter(is_published=True) # filter by created date in descending order
    # .objects.order_by('-list_date').filter(is_published=True)
    context=  {
        'quizs': quizs
    }

    return render(request, 'mcqapp/index3.html', context)
