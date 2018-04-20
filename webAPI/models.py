from django.db import models

class Convert(models.Model):
    unit_from = models.CharField(max_length=20)
    unit_to = models.CharField(max_length=20)
    conversion_factor = models.DecimalField(max_digits=6, decimal_places=4)