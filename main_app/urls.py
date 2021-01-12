from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('api/', views.api, name='api'),
    
    # EPISODES
    # path('episode/<int:episode_id>/', views.episode_detail, name='episode_detail'),
    
    # may not need these:
    # path('episode/create/', views.episode_create, name='episode_create'),
    # path('episode/<int:episode_id>/edit', views.episode_edit, name='episode_edit'),
    # path('episode/<int:episode_id>/delete', views.episode_delete, name='episode_delete'),

    # ACTOR BIOS
    path('bios/', views.bios_index, name='bios_index'),
    
    # may not need these:
    # path('bios/create/', views.bio_create, name='bio_create'),
    # path('bios/<int:bio_id>/edit', views.bio_edit, name='bio_edit'),
    # path('bios/<int:bio_id>/delete', views.bio_delete, name='bio_delete'),
]
