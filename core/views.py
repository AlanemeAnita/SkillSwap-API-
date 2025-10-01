from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello from Core app!")

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
