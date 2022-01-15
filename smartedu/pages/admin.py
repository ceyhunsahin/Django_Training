from django.contrib import admin
# from .models import Category
#
#
# @admin.register(Category)
# class CatAdmin(admin.ModelAdmin):
#     prepopulated_fields = { 'slug': ('name',) }

from .models import ContactFormMod


@admin.register(ContactFormMod)
class ContactAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'email': ('email',) }
# Register your models here.
