import datetime
import random
from celery import shared_task
from django.db import transaction
from django.db.models import Q
from matches.models import Match


@shared_task
def update_match_result():
    sample_results = list(range(10))
    with transaction.atomic():
        matches = Match.objects.filter(
            Q(
                match_schedule__lte=datetime.date.today()
            ) & 
            Q(
                match_schedule__gte=datetime.date.today() - datetime.timedelta(days=1)
            )
            ).all()
        for match in matches.iterator():
            match_result = [str(random.choice(sample_results)) for i in range(2)]
            match.match_result = ":".join(match_result)
        Match.objects.bulk_update(matches, ("match_result",))
