from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .models import CustomUser
from rest_framework.decorators import api_view, permission_classes
from .serializers import CustomUserSerializer, UserRegistrationSerializer, UserProfileUpdateSerializer


# Create your views here.
class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
class UserProfileView(generics.GenericAPIView):
    def get(self, request, username):
        try:
            user = CustomUser.objects.get(username=username)
            serializer = CustomUserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, username):
        try:
            user = CustomUser.objects.get(username=username)
            serializer = UserProfileUpdateSerializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except CustomUser.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]
        

# View to follow/unfollow users
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def follow_user(request, username):
    try:
        user_to_follow = CustomUser.objects.get(username=username)
        current_user = request.user
        if current_user == user_to_follow:
            return Response({'error': 'You cannot follow yourself.'}, status=status.HTTP_400_BAD_REQUEST)
        
        if current_user.is_following(user_to_follow):
            current_user.unfollow(user_to_follow)
            return Response({'status': f'Unfollowed {username}'}, status=status.HTTP_200_OK)
        else:
            current_user.follow(user_to_follow)
            return Response({'status': f'Followed {username}'}, status=status.HTTP_200_OK)
    except CustomUser.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unfollow_user(request, username):
    try:
        user_to_unfollow = CustomUser.objects.get(username=username)
        current_user = request.user
        if current_user == user_to_unfollow:
            return Response({'error': 'You cannot unfollow yourself.'}, status=status.HTTP_400_BAD_REQUEST)
        
        if current_user.is_following(user_to_unfollow):
            current_user.unfollow(user_to_unfollow)
            return Response({'status': f'Unfollowed {username}'}, status=status.HTTP_200_OK)
        else:
            return Response({'status': f'Not following {username}'}, status=status.HTTP_200_OK)
    except CustomUser.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    
    
# View to get followers and following lists
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def followers_list(request, username):
    try:
        user = CustomUser.objects.get(username=username)
        followers = user.followers.all()
        serializer = CustomUserSerializer(followers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except CustomUser.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def following_list(request, username):
    try:
        user = CustomUser.objects.get(username=username)
        following = user.following.all()
        serializer = CustomUserSerializer(following, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except CustomUser.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)