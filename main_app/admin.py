from django.contrib import admin
from .models import Performer, Play, Creator

# Register your models here.
class CreatorAdmin(admin.ModelAdmin):
    fields = ('name', 'title', 'bio', 'email')
    list_display = ['name', 'title', 'bio', 'email']

class PerformerAdmin(admin.ModelAdmin):
    fields = ('name', 'bio', 'imdb')
    list_display = ['name', 'bio', 'imdb']

admin.site.register(Performer, PerformerAdmin)
admin.site.register(Creator, CreatorAdmin)
admin.site.register(Play)
