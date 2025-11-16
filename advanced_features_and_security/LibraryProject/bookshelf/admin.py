from django.contrib import admin
from .models import Book, CustomUser
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_filter = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'date_of_birth')
    search_fields = ('username', 'email')

admin.site.register(Book, BookAdmin, CustomUser, CustomUserAdmin)