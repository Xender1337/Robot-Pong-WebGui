from django.db import models

# Create your models here.
class Raspberry (models.Model):
    label = models.CharField(max_length=255, unique=True, blank=False)
    status = models.PositiveIntegerField(default=0)
    programme = models.PositiveIntegerField(default=0)
    cadence = models.PositiveIntegerField(default=0)
    vitesse = models.PositiveIntegerField(default=0)