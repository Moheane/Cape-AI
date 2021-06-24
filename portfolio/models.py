from django.db import models


# Create your models here.
class personal_details(models.Model):
    name = models.CharField(unique=True, max_length=30)
    Surname = models.CharField(unique=True, max_length=30)
    Linkedin = models.CharField(max_length=30)
   
    location = models.CharField(max_length=30, default='Johannesburg')

    def __str__(self):
        return self.name

    