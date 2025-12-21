from django.urls import path, include
from .views import NotificationListView, NotificationCreateView, NotificationMarkAsReadView, NotificationDeleteView
from rest_framework.routers import DefaultRouter



urlpatterns = [
    path('notifications/', NotificationListView.as_view(), name='notification-list'),
    path('notifications/create/', NotificationCreateView.as_view(), name='notification-create'),
    path('notifications/<int:pk>/mark-as-read/', NotificationMarkAsReadView.as_view(), name='notification-mark-as-read'),
    path('notifications/<int:pk>/delete/', NotificationDeleteView.as_view(), name='notification-delete'),
]