from django.db import models

# Create your models here.


class IPAPIModel(models.Model):
    """Simple mock model."""
    name = models.CharField(max_length=30)
    value = models.IntegerField()
