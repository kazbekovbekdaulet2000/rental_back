from datetime import timedelta
from django.utils import timezone

def now_minus_28(): return timezone.now() - timedelta(days=28)