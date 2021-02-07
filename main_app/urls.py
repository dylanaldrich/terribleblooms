from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('tale/<int:tale_id>/', views.tale_detail, name='tale_detail'),
    path('performers/', views.performers, name='performers'),
]
