from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('play/<int:play_id>/', views.play_Detail, name='play_Detail'),
    path('performers/', views.performers, name='performers'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
