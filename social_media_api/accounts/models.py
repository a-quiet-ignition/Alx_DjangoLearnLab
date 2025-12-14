from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

#User model extending AbstractUser
class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)
    location = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.username
    