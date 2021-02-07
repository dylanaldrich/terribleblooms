from django.contrib import admin
from .models import Performer, Tale, Creator

# Register your models here.
admin.site.register(Performer)
admin.site.register(Tale)
admin.site.register(Creator)