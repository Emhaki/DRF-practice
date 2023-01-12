from .models import Blog
from .serializer import BlogSerializer
from rest_framework import generics

# Blog의 목록을 보여주는 역할
class BlogList(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

# Blog의 detail을 보여주는 역할
class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
