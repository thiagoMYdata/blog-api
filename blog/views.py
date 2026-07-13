from django.shortcuts import render
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

# Create your views here.
class APIListPost(generics.ListAPIView):    # GET all
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class APIDetailPost(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class APIUpdatePost(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class APIDestoryPost(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class APICreatePost(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer