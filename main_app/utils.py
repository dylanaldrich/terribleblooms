from datetime import datetime, timezone
from .models import Play

def check_Release_Date():
    plays = list(Play.objects.values())
    present = datetime.now(timezone.utc)

    for play in plays:
        if play['release_Date'] > present:
            plays.remove(play)
    
    return plays