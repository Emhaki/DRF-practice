from django.shortcuts import render

# Create your views here.
from .models import Blog
from .serializer import BlogSerializer
# APIView를 사용하기 위해 import
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# Blog list를 보여줄 때
class BlogList(APIView):

  def get(self, request):
    blogs = Blog.objects.all()
    # 여러 개의 객체를 serialization하기 위해 many = True로 설정
    serializer = BlogSerializer(blogs, many = True)
    return Response(serializer.data)

  # 새로운 blog 글을 작성할 때 
  def post(self, request):
    # request.data는 사용자의 입력 데이터
    serializer = BlogSerializer(data=request.data)
    if serializer.is_valid(): # 유효성 검사
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Blog detail을 보여주는 역할
class BlogDetail(APIView):
  
  # blog 객체 가져오기
  def get_object(self, pk): # get_object 선언
    try:
      return Blog.objects.get(pk=pk)
    except Blog.DoesNotExist:
      raise Http404
  
  # blog의 detail 보기
  def get(self, request, pk, format=None):
    blog = self.get_object(pk)
    serializer = BlogSerializer(blog)
    return Response(serializer.data)

  # blog 수정하기
  def put(self, request, pk, format=None):
    blog = self.get_object(pk)
    serializer = BlogSerializer(blog, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
  
  # blog 삭제하기
  def delete(self, request, pk, format=None):
    blog = self.get_object(pk)
    blog.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)