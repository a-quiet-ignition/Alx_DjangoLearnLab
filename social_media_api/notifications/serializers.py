from rest_framework import serializers
from .models import Notification


# Serializer for the Notification model
class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'actor', 'verb', 'target', 'timestamp']
        read_only_fields = ['id', 'timestamp']   
        
    def create(self, validated_data):
        notification = Notification.objects.create(**validated_data)
        return notification
    
    
