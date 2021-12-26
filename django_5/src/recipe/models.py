from django.db import models


class Student(models.Model) :
    first_name = models.CharField(max_length= 30)
    last_name = models.CharField(max_length=30)
    number = models.IntegerField()
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
# Create your models here.
