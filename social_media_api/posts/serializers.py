from rest_framework import serializers
from .models import Post, Comment


        
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
    
    