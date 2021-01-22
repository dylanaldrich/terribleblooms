from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Episode, Actor

# Create your views here.
def home(request):
    episodes = list(Episode.objects.values())
    latest_Episode = episodes.pop(0)
    context = {
        "episodes" : episodes, 
        "latest_Episode" : latest_Episode,
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def api(request):
    return JsonResponse({"status": 200})

def bios(request):
    context = {"actors" : Actor.objects.all()}
    return render(request, 'bios.html', context)

def episode_detail(request, episode_id):
    context = {'episode': Episode.objects.get(id=episode_id)}
    return render(request, 'episode.html', context)