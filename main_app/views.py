from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Play, Performer, Creator
from .utils import check_Release_Date

# HOME PAGE
def home(request):
    plays = check_Release_Date()
    latest_Play = {}

    if len(plays) > 0:
        latest_Play = plays.pop(0)

    context = {
        "plays" : plays, 
        "latest_Play" : latest_Play,
    }
    return render(request, 'home.html', context)

# ABOUT PAGE
def about(request):
    # context = {"creators" : Creator.objects.all()}
    return render(request, 'about.html')

# PERFORMERS PAGE
def performers(request):
    context = {"performers" : Performer.objects.all()}
    return render(request, 'performers.html', context)

# PLAY DETAIL PAGE
def play_Detail(request, play_id):
    context = {'play': Play.objects.get(id=play_id)}
    return render(request, 'play.html', context)