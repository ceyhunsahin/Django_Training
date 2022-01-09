from django.contrib import admin
from .models import Book, BookInstance, Genre, Author, Language, Author
# from tutorial_example.tuto.models import Author



admin.site.register(Genre)

admin.site.register(Language)
# Define the admin class
# class AuthorAdmin(admin.ModelAdmin):
#     pass
#
# # Register the admin class with the associated model
# admin.site.register(Author, AuthorAdmin)
#
# class BookAdmin(admin.ModelAdmin):
#     pass

# Register the Admin classes for BookInstance using the decorator


# Register your models here.
# class BookAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author', 'display_genre')
#
class BooksInline(admin.StackedInline) :
    model = Book
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

    inlines = [BooksInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book','status', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        ('Info', {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')

    inlines = [BooksInstanceInline]






