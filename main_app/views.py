from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.http import Http404
from django.core.exceptions import PermissionDenied
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from django.db.models import Prefetch
from .models import Play, Performer, Creator
from .utils import check_Release_Date

class HomeView(TemplateView):
    template_name = 'home.html'

    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        plays = check_Release_Date()

        if plays:
            context['latest_Play'] = plays[0]
            context['plays'] = plays[1:]

        return context

class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['creators'] = Creator.objects.select_related().all()
        return context

class PerformerListView(ListView):
    model = Performer
    template_name = 'performers.html'
    context_object_name = 'performers'

    def get_queryset(self):
        return (Performer.objects
                .prefetch_related(
                    Prefetch('plays', queryset=Play.objects.only('id', 'name'))
                )
                .all())

class PlayDetailView(DetailView):
    model = Play
    template_name = 'play.html'
    context_object_name = 'play'
    pk_url_kwarg = 'pk'

    def get_queryset(self):
        return (Play.objects
                .prefetch_related(
                    Prefetch('performers', queryset=Performer.objects.only('id', 'name'))
                ))

# Error handlers
def bad_request(request, exception):
    return render(request, '400.html', status=400)

def permission_denied(request, exception):
    return render(request, '403.html', status=403)

def page_not_found(request, exception):
    return render(request, '404.html', status=404)

def server_error(request):
    return render(request, '500.html', status=500)

# Custom exception middleware
class CustomExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self, request, exception):
        if isinstance(exception, Http404):
            return page_not_found(request, exception)
        elif isinstance(exception, PermissionDenied):
            return permission_denied(request, exception)
        return None
