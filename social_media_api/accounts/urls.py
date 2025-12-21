from django.urls import path, include
from .views import UserRegistrationView, UserLoginView, UserProfileView, follow_user, UserListView, unfollow_user


urlpatterns = [    
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('profile/<str:username>/', UserProfileView.as_view(), name='user-profile'),
    path('follow/<int:user_id>/', follow_user, name='follow-user'),
    path('unfollow/<int:user_id>/', unfollow_user, name='unfollow-user'),
    path('users/', UserListView.as_view(), name='user-list'),
]