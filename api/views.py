from django.shortcuts import render
from rest_framework import views
from .serializers import *
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

# Create your views here.


class BookView(generics.ListCreateAPIView, generics.DestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class AuthorView(generics.ListCreateAPIView, generics.DestroyAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    
    def create(self, request, *args, **kwargs):
        # Initialize an empty list to store serializer instances
        serializer_instances = []

        # Iterate over each author object in the request data list
        for author_data in request.data:
            # Pass each author object to the serializer
            serializer = self.get_serializer(data=author_data)
            # Validate the serializer
            serializer.is_valid(raise_exception=True)
            # Save the serializer instance in the list
            serializer_instances.append(serializer)
            # Perform creation for each author object
            self.perform_create(serializer)

        # Get the success headers for the last serializer instance
        headers = self.get_success_headers(serializer_instances[-1].data)
        
        # Return a response with the data of all created authors
        return Response([serializer.data for serializer in serializer_instances], status=status.HTTP_201_CREATED, headers=headers)

class CategoryView(generics.ListCreateAPIView, generics.DestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class PublisherView(generics.ListCreateAPIView, generics.DestroyAPIView):
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all()
    def create(self, request, *args, **kwargs):
        # Initialize an empty list to store serializer instances
        serializer_instances = []

        # Iterate over each author object in the request data list
        for author_data in request.data:
            # Pass each author object to the serializer
            serializer = self.get_serializer(data=author_data)
            # Validate the serializer
            serializer.is_valid(raise_exception=True)
            # Save the serializer instance in the list
            serializer_instances.append(serializer)
            # Perform creation for each author object
            self.perform_create(serializer)

        # Get the success headers for the last serializer instance
        headers = self.get_success_headers(serializer_instances[-1].data)
        
        # Return a response with the data of all created authors
        return Response([serializer.data for serializer in serializer_instances], status=status.HTTP_201_CREATED, headers=headers)




