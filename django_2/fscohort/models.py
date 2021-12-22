from django.db import models


# Create your models here.

class Student (models.Model):
    prenom = models.CharField (max_length=50)
    last_name = models.CharField (max_length=23)
    number = models.IntegerField ()

    def __str__(self):
        return self.prenom + ' ' + self.last_name
