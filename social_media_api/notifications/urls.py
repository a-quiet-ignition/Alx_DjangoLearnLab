from django.urls import path, include
from .views import NotificationListView, NotificationCreateView, NotificationMarkAsReadView, NotificationDeleteView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'notifications', NotificationListView, basename='notification-list')


urlpatterns = [
    path('', include(router.urls)),
    path('notifications/create/', NotificationCreateView.as_view(), name='notification-create'),
    path('notifications/<int:pk>/mark-as-read/', NotificationMarkAsReadView.as_view(), name='notification-mark-as-read'),
    path('notifications/<int:pk>/delete/', NotificationDeleteView.as_view(), name='notification-delete'),
]