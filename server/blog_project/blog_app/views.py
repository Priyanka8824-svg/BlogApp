from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status
from .models import Blog
from .serializers import BlogSerializer
from account.authenticate import CustomAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.views import APIView


User = get_user_model()

# Create your views here.
import logging
logger = logging.getLogger(__name__)

class BlogCreateAPI(generics.ListCreateAPIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by = self.request.user)
        logger.info('New Blog Added....!!!!')
       
class BlogListAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        blog = Blog.objects.filter(created_by = request.user)
        serializer = BlogSerializer(blog, many=True)
        return Response(data=serializer.data)

class BlogUpdateAPI(generics.UpdateAPIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    serializer_class=BlogSerializer
    queryset=Blog.objects.all()

class BlogDeleteAPI(generics.DestroyAPIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    serializer_class=BlogSerializer
    queryset=Blog.objects.all()

class BlogRetrieveAPI(generics.RetrieveAPIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    serializer_class=BlogSerializer
    queryset=Blog.objects.all()