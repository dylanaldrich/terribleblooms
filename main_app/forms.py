from django.forms import ModelForm
from .models import Performer, Play, Creator

class Performer_Form(ModelForm):
    class Meta:
        model = Performer
        fields = ['name', 'bio', 'photo', 'website', 'facebook', 'twitter', 'instagram']

class Play_Form(ModelForm):
    class Meta:
        model = Play
        fields = ['name', 'description', 'image', 'external_link']

class Creator_Form(ModelForm):
    class Meta:
        model = Creator
        fields = ['name', 'title', 'bio', 'photo', 'email', 'website', 'facebook', 'twitter', 'instagram']