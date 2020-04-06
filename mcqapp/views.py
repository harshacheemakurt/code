from django.shortcuts import render,HttpResponse,redirect
# from .models import Quiz
from mcqapp.models import Quiz
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import  User


# Create your views here.
def home(request):
    return render(request,'mcqapp/home.html')

def login(request):
    if request.method=='POST':
        username= request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password= password)
        if user is not None:
            auth.login(request,user)
            return redirect('index1')
        else:
            return redirect('login')
    return  render(request, 'mcqapp/login.html')

def register(request):
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username= username).exists():

                return redirect('register')
            else:
                user =User.objects.create_user(username= username, password= password,email= email, first_name=first_name,last_name=last_name)
                user.save()
                return redirect('login')
        else:
            return redirect('register')
    else:
        return  render(request,'mcqapp/register.html')

value =0
def index1(request):
    global value
    # if user is not None:
    if request.user.is_authenticated:

        questions = Quiz.objects.all()

        if request.method == 'POST':
            for question in questions:
                actual_answer = question.answers
                select_option = request.POST.get(str(question.id))

                if (select_option == actual_answer):
                    value += 1
            # user_model = Quiz.objects.
            context1 = {'value': value}
            return render(request,'mcqapp/answer.html',context1)
        else:




            context = {'questions': questions}
            return render(request, 'mcqapp/index.html', context)

