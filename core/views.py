from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import Post, Comment
from .models import Post
from .serializers import PostSerializer, CommentSerializer
from django.http import HttpResponse
from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Welcome to SkillSwap API — deployed successfully 🎉"})

def home(request):
    return HttpResponse("Hello from Core app!")

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)






