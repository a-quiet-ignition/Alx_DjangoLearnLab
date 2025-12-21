from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Create your models here.
class Notification(models.Model):
    recipient = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, related_name='notifications')
    actor = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, related_name='actions')
    verb = models.CharField(max_length=255)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    target_id = models.PositiveIntegerField(null=True, blank=True)
    target = GenericForeignKey('content_type', 'target_id')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Notification for {self.recipient.username}: {self.verb}'