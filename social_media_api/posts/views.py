from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from social_media_api.notifications.models import Notification
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

# Post Views
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
     # Add filtering and search
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # Search in title and content
    search_fields = ['title', 'content', 'author__username']
    
    # Allow filtering by author
    filterset_fields = ['author', 'created_at']
    
    # Allow ordering by date or title
    ordering_fields = ['published_date', 'title']
    ordering = ['-created_at'] 
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        
        
# Comment Views
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
     # Add filtering and search
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # Allow ordering by date
    ordering_fields = ['created_at']
    ordering = ['-created_at']
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        

# View to generete posts feed for a user from followed users
class UserFeedViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        user = self.request.user
        following_users = user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at')
    
    
# Views for handling liking and unliking posts
class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
    def get_queryset(self):
        user = self.request.user
        return Like.objects.filter(user=user)
    
    @action(detail=False, methods=['post'])
    def like(self, request, post_pk=None):
        post = get_object_or_404(Post, pk=post_pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        
        if created:
            if post.author != request.user:
                Notification.objects.create(
                    recipient=post.author,
                    sender=request.user,
                    verb='liked your post',
                    target_object_id=post.id
                )
            
            return Response({
                'status': 'Post liked',
                'post_id': post.id,
                'user': request.user.username
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                'status': 'You have already liked this post',
                'post_id': post.id
            }, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['post'])
    def unlike(self, request, pk=None):
        like = self.get_object()
        if like.user != request.user:
            return Response({'error': 'You can only unlike your own likes.'}, status=status.HTTP_403_FORBIDDEN)
        like.delete()
        return Response({'status': 'Post unliked'}, status=status.HTTP_200_OK)
    
    