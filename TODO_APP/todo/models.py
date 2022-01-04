from django.db import models

from django.db import models


# class Student (models.Model):
#     first_name = models.CharField (max_length=30)
#     last_name = models.CharField (max_length=30)
#     number = models.IntegerField ()
#
#     def __str__(self):
#         return self.first_name
# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    class Meta:
     #ordering = ('-created_date',) ya boyle
     ordering = ['-created_date']

    def __str__(self):
        return self.title
