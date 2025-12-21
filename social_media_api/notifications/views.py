from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.exceptions import PermissionDenied
from .models import Notification
from .serializers import NotificationSerializer

# Create your views here.

# View to list notifications for a user
class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Notification.objects.filter(recipient=user).order_by('-timestamp')
    
# View to create a new notification
class NotificationCreateView(generics.CreateAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save()
        
# View to mark a notification as read
class NotificationMarkAsReadView(generics.UpdateAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Notification.objects.all()
    
    def get_object(self):
        notification = super().get_object()
        if notification.recipient != self.request.user:
            raise PermissionDenied("You do not have permission to mark this notification.")
        return notification
    
    def perform_update(self, serializer):
        serializer.instance.read = True
        serializer.instance.save()
    
# View to delete a notification
class NotificationDeleteView(generics.DestroyAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Notification.objects.all()
    
    def get_object(self):
        notification = super().get_object()
        if notification.recipient != self.request.user:
            raise PermissionDenied("You do not have permission to delete this notification.")
        return notification
    
