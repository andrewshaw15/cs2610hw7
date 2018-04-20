import datetime

from django.shortcuts import render
from django.utils import timezone

def index(request):
    return render(request, 'simplePage/index.html', {
        'current_date' : timezone.now(),
        'past_date' : timezone.now() - datetime.timedelta(days=5),
    })