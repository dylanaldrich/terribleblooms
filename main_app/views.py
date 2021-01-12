from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def api(request):
    return JsonResponse({"status": 200})

def bios(request):
    return render(request, 'bios.html')

def episode_detail(request, episode_id):
    episode = Episode.objects.get(id=episode_id)
    return render(request, 'episode.html', episode)