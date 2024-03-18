from django.shortcuts import render
from rest_framework import views
from .serializers import *
from rest_framework import generics
# Create your views here.


class BookView(generics.ListCreateAPIView, generics.DestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class AuthorView(generics.ListCreateAPIView, generics.DestroyAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

class CategoryView(generics.ListCreateAPIView, generics.DestroyAPIView):
    serializer_class = Category.objects.all()
    queryset = Category.objects.all()

class PublisherView(generics.ListCreateAPIView, generics.DestroyAPIView):
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all()



