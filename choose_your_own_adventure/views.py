from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404
from django.views import View
from choose_your_own_adventure.forms import CustomAuthenticationForm, CustomUserCreationForm
from .models import User
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

def home(request: HttpRequest):
    return render(request, 'home.html')

def register(request: HttpRequest):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('make_choice', choice=user.last_choice)
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})

def user_login(request: HttpRequest):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('make_choice', choice=user.last_choice)
    else:
        form = CustomAuthenticationForm()
    
    return render(request, 'registration/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
def make_choice(request: HttpRequest, choice: str):
    user = request.user
    user.last_choice = choice
    
    if request.GET.get('reset') or choice != "start":
        user.clicks += 1
    else:
        user.clicks = 0
        
    user.save()
    
    context = {'choice': choice, "clicks": user.clicks}
    
    if user.clicks > 10 and choice in ("start", "portal"):
        return render(request, 'secret.html', context)
    
    return render(request, f'{choice}.html', context)
