from django.shortcuts import render,HttpResponse
# from .models import Quiz
from mcqapp.models import Quiz


# Create your views here.

value =0
def index1(request):
    questions = Quiz.objects.all()
    global value
    if request.method == 'POST':
        for question in questions:
            actual_answer = question.answers
            select_option = request.POST.get(str(question.id))

            if (select_option == actual_answer):
                value += 1
        context1 = {'value': value}
        return render(request,'mcqapp/answer.html',context1)
    else:



        context = {'questions': questions}
        return render(request, 'mcqapp/index.html', context)

