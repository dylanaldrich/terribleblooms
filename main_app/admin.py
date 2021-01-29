from django.contrib import admin
from .models import Actor, Episode, Creator

# Register your models here.
admin.site.register(Actor)
admin.site.register(Episode)
admin.site.register(Creator)