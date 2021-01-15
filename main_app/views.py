from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Episode, Actor

# Create your views here.
def home(request):
    # use for now:
    # return render(request, 'home.html')
    episodes = Episode.objects.all()
    context = {
        "episodes" : episodes
    }
    print("Episodes", episodes)
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def api(request):
    return JsonResponse({"status": 200})

def bios(request):
    # use for now:
    return render(request, 'bios.html')
    # bios = Bio.objects.get()
    # return render(request, 'bios.html', bios)

def episode_detail(request, episode_id):
    # episode = Episode.objects.get(id=episode_id)
    context = {'episode': episode_id}
    return render(request, 'episode.html', context)