from django.contrib import admin
from .models import Performer, Play, Creator
from django_quill.widgets import QuillWidget
from django import forms

# Register your models here.

class CreatorAdminForm(forms.ModelForm):
    class Meta:
        model = Creator
        fields = ('name', 'title', 'bio', 'email')
        widgets = {
            'bio': QuillWidget(),
        }

class CreatorAdmin(admin.ModelAdmin):
    form = CreatorAdminForm
    list_display = ['name']


class PerformerAdminForm(forms.ModelForm):
    class Meta:
        model = Performer
        fields = ('name', 'bio', 'imdb')
        widgets = {
            'bio': QuillWidget(),
        }

class PerformerAdmin(admin.ModelAdmin):
    form = PerformerAdminForm
    list_display = ['name']

admin.site.register(Performer, PerformerAdmin)
admin.site.register(Creator, CreatorAdmin)
class PlayAdminForm(forms.ModelForm):
    class Meta:
        model = Play
        fields = ('name', 'description', 'audioFile', 'image', 'performers', 'release_Date')
        widgets = {
            'description': QuillWidget(),
        }

class PlayAdmin(admin.ModelAdmin):
    form = PlayAdminForm
    list_display = ['name', 'release_Date']

admin.site.register(Play, PlayAdmin)
