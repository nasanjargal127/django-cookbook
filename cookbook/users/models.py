from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    status = models.CharField()

    def __str__(self):
        return self.name
