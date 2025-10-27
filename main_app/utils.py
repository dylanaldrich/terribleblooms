from django.utils import timezone
from django.db.models import Prefetch
from .models import Play, Performer

def check_Release_Date():
    present = timezone.now()
    return (Play.objects
            .filter(release_Date__lte=present)
            .prefetch_related(
                Prefetch('performers', queryset=Performer.objects.only('name', 'id'))
            )
            .order_by('-release_Date'))
