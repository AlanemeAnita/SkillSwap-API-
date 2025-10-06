from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from .models import Post, UserProfile, Comment
from core.models import UserProfile

class PostTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.profile = UserProfile.objects.create(user=self.user, bio="Test bio")
        self.client = APIClient()
        self.client.login(username="testuser", password="password123")

    def test_create_post(self):
        response = self.client.post("/api/posts/", {
            "title": "My Post",
            "content": "Hello world!",
            "user": self.profile.id   # ✅ pass UserProfile ID
        })
        self.assertEqual(response.status_code, 201)

    def test_create_post_invalid(self):
        response = self.client.post("/api/posts/", {"title": "Hi", "content": ""})
        self.assertEqual(response.status_code, 400)

class CommentTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='pass123')
        self.profile = UserProfile.objects.create(user=self.user)
        self.post = Post.objects.create(title='Test Post', content='Some content', user=self.profile)

    def test_create_comment(self):
        data = {'post': self.post.id, 'user': self.profile.id, 'content': 'Nice post!'}
        response = self.client.post('/api/comments/', data)
        self.assertEqual(response.status_code, 201)
