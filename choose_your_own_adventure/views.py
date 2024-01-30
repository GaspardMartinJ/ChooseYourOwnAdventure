from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from choose_your_own_adventure.forms import CustomAuthenticationForm, CustomUserCreationForm
from .models import User
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')
    

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('make_choice', choice=user.last_choice)
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('make_choice', choice=user.last_choice)
    else:
        form = CustomAuthenticationForm()
    
    return render(request, 'registration/login.html', {'form': form})

@login_required
def make_choice(request, choice):
    
    user = request.user
    user.last_choice = choice
    user.save()
    
    context = {'choice': choice}
    
    return render(request, f'{choice}.html', context)
