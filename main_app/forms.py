from django.forms import ModelForm
from .models import Actor, Episode, Creator

class Actor_Form(ModelForm):
    class Meta:
        model = Actor
        fields = ['name', 'bio', 'photo', 'website', 'facebook', 'twitter', 'instagram']

class Episode_Form(ModelForm):
    class Meta:
        model = Episode
        fields = ['name', 'description', 'image', 'external_link']

class Creator_Form(ModelForm):
    class Meta:
        model = Creator
        fields = ['name', 'bio', 'photo', 'email', 'website', 'facebook', 'twitter', 'instagram']