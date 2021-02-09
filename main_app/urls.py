from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('play/<int:play_id>/', views.play_detail, name='play_detail'),
    path('performers/', views.performers, name='performers'),
]
