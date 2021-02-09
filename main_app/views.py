from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Play, Performer, Creator

# Create your views here.
def home(request):
    plays = list(Play.objects.values())
    latest_Play = {}

    if len(plays) > 0:
        latest_Play = plays.pop(0)

    context = {
        "plays" : plays, 
        "latest_Play" : latest_Play,
    }
    return render(request, 'home.html', context)

def about(request):
    context = {"creators" : Creator.objects.all()}
    return render(request, 'about.html', context)

def performers(request):
    context = {"performers" : Performer.objects.all()}
    return render(request, 'performers.html', context)

def play_detail(request, play_id):
    context = {'play': Play.objects.get(id=play_id)}
    return render(request, 'play.html', context)