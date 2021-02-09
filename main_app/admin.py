from django.contrib import admin
from .models import Performer, Play, Creator

# Register your models here.
admin.site.register(Performer)
admin.site.register(Play)
admin.site.register(Creator)