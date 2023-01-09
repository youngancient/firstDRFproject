
from rest_framework import generics
from .models import Blog
from .serializers import BlogSerializer
# Create your views here.

class ListBlogView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class CreateBlogView(generics.CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer



