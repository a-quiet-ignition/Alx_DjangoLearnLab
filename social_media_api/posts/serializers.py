from rest_framework import serializers
from .models import Post, Comment, Like


        
# Post Serializers
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        
    def create(self, validated_data):
        post = Post.objects.create(**validated_data)
        return post
        

# Comment Serializers
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        
    def create(self, validated_data):
        comment = Comment.objects.create(**validated_data)
        return comment
    

# Like Serializers
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
        
    def create(self, validated_data):
        like = Like.objects.create(**validated_data)
        return like