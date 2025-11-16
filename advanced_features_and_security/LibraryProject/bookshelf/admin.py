from django.contrib import admin
from .models import Book, CustomUser
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_filter = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    
class UserAdmin(admin.ModelAdmin):
    date_of_birth = admin.DateField()
    profile_picture = admin.ImageField()

admin.site.register(Book, BookAdmin)