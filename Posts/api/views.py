import imp
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PostsSerializer
from .models import Posts

# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostsSerializer
    queryset = Posts.objects.all()
