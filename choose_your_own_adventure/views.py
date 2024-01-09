from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Player
from django.shortcuts import redirect

def start(request):
    context = {}
    return render(request, 'start.html', context=context)

def make_choice(request, choice):
    # Process the user's choice and provide context data
    context = {'choice': choice}
    
    return render(request, f'{choice}.html', context)
