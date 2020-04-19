from django.db import models


class Person(models.Model):
    email = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
