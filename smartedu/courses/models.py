from django.db import models
from teachers.models import Teacher



class Category(models.Model):
    name = models.CharField(max_length=50, null = True)
    slug = models.SlugField(max_length=50, unique=True, null=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50, null = True)
    slug = models.SlugField(max_length=50, unique=True, null=True)

    def __str__(self):
        return self.name


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length= 200, help_text='Enter Course Name', unique=True, verbose_name='Course Name')
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category,null=True, on_delete=models.DO_NOTHING)
    tags = models.ManyToManyField(Tag, blank= True, null= True)
    image = models.ImageField(upload_to='courses/%Y/%m/%d/', default="courses/dummy_image_default.png")
    date = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)
    teacher = models.ForeignKey(Teacher, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

