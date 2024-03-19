from django.shortcuts import render
from rest_framework import views
from .serializers import *
from rest_framework import generics, viewsets
from rest_framework import status
from rest_framework.response import Response

# Create your views here.


class BookView(generics.ListCreateAPIView, generics.DestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

#----------------------------------------------------------------------------------------------------------------------

class AuthorView(generics.ListCreateAPIView, generics.DestroyAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    
    def create(self, request, *args, **kwargs):
        serializer_instances = []

        for author_data in request.data:
            serializer = self.get_serializer(data=author_data)
            serializer.is_valid(raise_exception=True)
            serializer_instances.append(serializer)
            self.perform_create(serializer)
        headers = self.get_success_headers(serializer_instances[-1].data)
        
        return Response([serializer.data for serializer in serializer_instances], status=status.HTTP_201_CREATED, headers=headers)
    

class AuthorViewFind(viewsets.ViewSet):
    def retrieve(self, request, pk=None, *args, **kwargs):
        author = kwargs.get('author')
        author = author.replace("+", " ")  # Corrected line
        instance = Author.objects.filter(name=author).first()
        if instance:
            ser = AuthorSerializer(instance)
            return Response({"id":ser.data['id']})
        else:
            return Response({"message": "Author not found"}, status=404)

#----------------------------------------------------------------------------------------------------------------------


class CategoryView(generics.ListCreateAPIView, generics.DestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    def create(self, request, *args, **kwargs):
        serializer_instances = []

        for Category_data in request.data:
            serializer = self.get_serializer(data=Category_data)
            serializer.is_valid(raise_exception=True)
            serializer_instances.append(serializer)
            self.perform_create(serializer)
        headers = self.get_success_headers(serializer_instances[-1].data)
        
        return Response([serializer.data for serializer in serializer_instances], status=status.HTTP_201_CREATED, headers=headers)
    
    
class CategoryViewFind(viewsets.ViewSet):
    def retrieve(self, request, pk=None, *args, **kwargs):
        category = kwargs.get('category')
        category = category.replace("+", " ")  # Corrected line
        instance = Category.objects.filter(name=category).first()
        if instance:
            ser = CategorySerializer(instance)
            return Response({"id":ser.data['id']})
        else:
            return Response({"message": "Category not found"}, status=404)


#----------------------------------------------------------------------------------------------------------------------

class PublisherView(generics.ListCreateAPIView, generics.DestroyAPIView):
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all()
    def create(self, request, *args, **kwargs):
        serializer_instances = []
        for author_data in request.data:
            serializer = self.get_serializer(data=author_data)
            serializer.is_valid(raise_exception=True)
            serializer_instances.append(serializer)
            self.perform_create(serializer)
        headers = self.get_success_headers(serializer_instances[-1].data)
        return Response([serializer.data for serializer in serializer_instances], status=status.HTTP_201_CREATED, headers=headers)
    
class PublisherViewFind(viewsets.ViewSet):
    def retrieve(self, request, pk=None, *args, **kwargs):
        publisher = kwargs.get('publisher')
        print(publisher)
        publisher = publisher.replace("+", " ")  # Corrected line
        instance = Publisher.objects.filter(name=publisher).first()
        if instance:
            ser = PublisherSerializer(instance)
            return Response({"id":ser.data['id']})
        else:
            return Response({"message": "publisher not found"}, status=404)




