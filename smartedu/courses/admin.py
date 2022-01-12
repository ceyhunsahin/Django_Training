from django.contrib import admin

from .models import Course, Category,Tag

# admin.site.register(Course)
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'available', 'date')
    # list_filter = ('available',)
    search_fields = ('name','description')
    list_editable = ('available',)
    # filter_horizontal = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug' : ('name',) }


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug' : ('name',) }


# Register your models here.
