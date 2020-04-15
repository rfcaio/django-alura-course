from datetime import datetime

from django.db import models


class Recipe(models.Model):
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(blank=True, default=datetime.now)
    ingredients = models.TextField()
    name = models.CharField(max_length=200)
    portions = models.CharField(max_length=100)
    preparation_mode = models.TextField()
    preparation_time = models.IntegerField()

    def __str__(self):
        return self.name
