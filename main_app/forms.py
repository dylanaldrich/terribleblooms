from django.forms import ModelForm
from .models import Actor, Episode

class Actor_Form(ModelForm):
    class Meta:
        model = Actor
        fields = ['name', 'bio', 'photo', 'website', 'facebook', 'twitter', 'instagram']

class Episode_Form(ModelForm):
    class Meta:
        model = Episode
        fields = ['name', 'description', 'image', 'external_link']