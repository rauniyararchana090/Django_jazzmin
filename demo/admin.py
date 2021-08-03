from django.contrib import admin
from .models import Book
# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    list_display = (
          'name',
          'author',
          'publication',
          'is_published',
          'published_at',
    )
    list_filter = (
        'is_published',
        'published_at',
        
    )