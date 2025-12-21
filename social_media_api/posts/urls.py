from django.urls import path, include
from .views import PostViewSet, CommentViewSet, UserFeedViewSet, LikeViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')


urlpatterns = [
    path('', include(router.urls)),
    path('feed/', UserFeedViewSet.as_view({'get': 'list'}), name='user-feed'),
    path('posts/<int:pk>/like/', LikeViewSet.as_view({'post': 'like'}), name='post-like'),
    path('posts/<int:pk>/unlike/', LikeViewSet.as_view({'post': 'unlike'}), name='post-unlike'),
]
