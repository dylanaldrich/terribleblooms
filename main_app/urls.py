from django.urls import path, re_path
from django.views.decorators.cache import cache_page
from . import views
from django.conf import settings
from django.conf.urls.static import static

# API version prefix
API_VERSION = 'v1'

urlpatterns = [
    path('', cache_page(60 * 15)(views.HomeView.as_view()), name='home'),  # Cache for 15 minutes
    path('about/', cache_page(60 * 60)(views.AboutView.as_view()), name='about'),  # Cache for 1 hour
    path(f'{API_VERSION}/play/<int:pk>/', views.PlayDetailView.as_view(), name='play_Detail'),
    path('artists/', cache_page(60 * 60)(views.PerformerListView.as_view()), name='artists'),  # Cache for 1 hour
]

# Error handlers
handler400 = 'main_app.views.bad_request'
handler403 = 'main_app.views.permission_denied'
handler404 = 'main_app.views.page_not_found'
handler500 = 'main_app.views.server_error'

# Only add static/media serving in DEBUG mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
