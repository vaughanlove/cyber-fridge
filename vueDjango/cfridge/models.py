from django.db import models

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=140)
    url = models.CharField(max_length=140)

    def __str__(self):
        return self.name
