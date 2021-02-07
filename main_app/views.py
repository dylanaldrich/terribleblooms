from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Tale, Performer, Creator

# Create your views here.
def home(request):
    tales = list(Tale.objects.values())
    latest_Tale = {}

    if len(tales) > 0:
        latest_Tale = tales.pop(0)

    context = {
        "tales" : tales, 
        "latest_Tale" : latest_Tale,
    }
    return render(request, 'home.html', context)

def about(request):
    context = {"creators" : Creator.objects.all()}
    return render(request, 'about.html', context)

def performers(request):
    context = {"performers" : Performer.objects.all()}
    return render(request, 'performers.html', context)

def tale_detail(request, tale_id):
    context = {'tale': Tale.objects.get(id=tale_id)}
    return render(request, 'tale.html', context)