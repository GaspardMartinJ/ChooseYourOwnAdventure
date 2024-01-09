from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import User
from django.shortcuts import redirect

def start(request):
    context = {}
    return render(request, 'start.html', context=context)

def make_choice(request, choice):
    
    user = request.user
    user.last_choice = choice
    user.save()
    
    context = {'choice': choice}
    
    return render(request, f'{choice}.html', context)
