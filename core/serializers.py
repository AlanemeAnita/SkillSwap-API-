from rest_framework import serializers
from .models import Post, UserProfile, Skill

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'user', 'content', 'created_at']

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)  # nested comments

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'user', 'created_at', 'comments']

    # Simple validation: title must not be empty
    def validate_title(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError("Title must be at least 3 characters long.")
        return value

