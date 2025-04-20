from django.shortcuts import render, redirect
from . import models as quiz_models
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="quiz:login_user")
def index(request):
    question = quiz_models.Question.objects.all().order_by("id")
    # choice = quiz_models.Choices.objects.filter(question=question)
    
    context = {
        "question": question,
        # "choice": choice 
        
    }
    
    return render(request, "index.html", context)

def calculate_score(request):
    question = quiz_models.Question.objects.all().order_by("id")
    score = 0
    if request.method == "POST":
        for quest in question:
            selected_choice_id = request.POST.get(f"choice_{quest.id}")
            
            if selected_choice_id:
                try:
                    selected_choice = quiz_models.Choices.objects.get(id=selected_choice_id)
                
                    if selected_choice.is_correct:
                        score += 2
                        
                except quiz_models.Choices.DoesNotExist:
                    pass
                
    return redirect(to="quiz:result_page")

def result_page(request):
    return render(request, 'result.html')
                    
def login_user(request):
    if request.user.is_authenticated:
        return request("quiz:index")
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("pswd")
        
        my_user = authenticate(username=username, password=password)
        
        if my_user is not None:
            login(request, my_user)
            messages.success(request, "Login Successful!!!")
            return redirect(to="quiz:index")
        else:
            messages.error(request, "There was a problem logging you in\nCheck login credentials")
            return redirect(to="quiz:login_user")
        
    return render(request, 'login.html')
