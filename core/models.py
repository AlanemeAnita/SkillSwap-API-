from django.db import models
from django.contrib.auth.models import User  

class Skill(models.Model):  
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class UserProfile(models.Model):  
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField(blank=True)
    skills = models.ManyToManyField(Skill, related_name="users", blank=True)

    def __str__(self):
        return self.user.username

class Post(models.Model):  
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
