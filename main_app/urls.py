from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('api/', views.api, name='api'),
    path('bios/', views.bios, name='bios'),
    path('episode/<int:episode_id>/', views.episode_detail, name='episode_detail'),
]
