# from django.db import models
# class Category(models.Model):
#     name = models.CharField(max_length=50, null = True)
#     slug = models.SlugField(max_length=50, unique=True, null=True)
#
#     def __str__(self):
#         return self.name
# Create your models here.
from django.db import models
from phone_field import PhoneField

class ContactFormMod(models.Model):
    first_name = models.CharField(max_length=100, help_text='First Name')
    last_name = models.CharField(max_length=100, help_text='Last Name')
    email = models.EmailField(help_text=' Your Email')
    phone = PhoneField(blank=True, help_text='Contact phone number')
    message = models.TextField()

    def __str__(self):
        return self.email
