from datetime import datetime, timezone
from .models import Play

def check_Release_Date():
    plays = list(Play.objects.all())
    present = datetime.now(timezone.utc)

    # Filter out plays that haven't been released yet
    return [play for play in plays if play.release_Date <= present]
