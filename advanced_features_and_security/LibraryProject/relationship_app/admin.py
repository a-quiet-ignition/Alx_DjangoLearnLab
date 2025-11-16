from django.contrib import admin

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    date_of_birth = admin.DateField()
    profile_picture = admin.ImageField()