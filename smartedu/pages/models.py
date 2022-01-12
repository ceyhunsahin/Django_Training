from django.db import models
class Category(models.Model):
    name = models.CharField(max_length=50, null = True)
    slug = models.SlugField(max_length=50, unique=True, null=True)

    def __str__(self):
        return self.name
# Create your models here.
