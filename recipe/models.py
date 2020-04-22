from datetime import datetime

from django.db import models

from person.models import Person


class Recipe(models.Model):
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(blank=True, default=datetime.now)
    image = models.ImageField(blank=True, upload_to='fotos/%d/%m/%Y')
    ingredients = models.TextField()
    is_published = models.BooleanField(default=False)
    name = models.CharField(max_length=200)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    portions = models.CharField(max_length=100)
    preparation_mode = models.TextField()
    preparation_time = models.IntegerField()

    def __str__(self):
        return self.name
