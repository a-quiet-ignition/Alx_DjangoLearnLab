from django.urls import path, include
from .views import UserRegistrationView, UserLoginView, UserProfileView, PostViewSet, CommentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [    
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('profile/<str:username>/', UserProfileView.as_view(), name='user-profile'),
    path('', include(router.urls)),
]