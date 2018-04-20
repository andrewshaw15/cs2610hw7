#from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse

from .models import Convert

def index(request):
    value1 = request.GET['value']
    unit1 = request.GET['from']
    unit2 = request.GET['to']

    if not value1:
        return JsonResponse({"error": "Please enter a number"})

    db_row = Convert.objects.get(unit_from=unit1)
    db_cell = db_row.conversion_factor
    value2 = float(value1) * float(db_cell)

    return JsonResponse({"units": unit2, "value": value2})

def init(request):
    Convert.objects.all().delete()
    c1 = Convert(unit_from = "lbs", unit_to = "t_oz", conversion_factor = 14.5833)
    c1.save()
    c2 = Convert(unit_from = "kg", unit_to = "t_oz", conversion_factor = 32.1507)
    c2.save()
    return HttpResponseRedirect(reverse('simplePage:index'))