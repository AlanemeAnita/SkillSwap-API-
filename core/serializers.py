from rest_framework import serializers
from .models import Post, UserProfile, Skill

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "title", "content", "created_at", "user"]

    # Simple validation: title must not be empty
    def validate_title(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError("Title must be at least 3 characters long.")
        return value
