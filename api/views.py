from django.shortcuts import render
from rest_framework import views
from .serializers import *
from rest_framework import generics, viewsets
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render
from tablib import Dataset
from .resources import BookR  # Assuming BookR is defined in resources.py within the same app
from django.contrib import messages
import io
import csv
import datetime

# Create your views here.


class BookView(generics.ListCreateAPIView, generics.DestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def create(self, request, *args, **kwargs):
        validated_data = request.data
        author_data = validated_data.pop('author', None)
        publisher_data = validated_data.pop('publisher', None)
        category = validated_data.pop('category', None)

        if author_data:
            author, _ = Author.objects.get_or_create(name=author_data['name']).first()
            validated_data['author'] = author.id

        if publisher_data:
            publisher, _ = Publisher.objects.get_or_create(name=publisher_data['name'])
            validated_data['publisher'] = publisher[0].id
        if category:
            ccategory, _ = Category.objects.get_or_create(name=category['name'])
            validated_data['category'] = ccategory[0].id

        serializer = self.get_serializer(data=validated_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    


#----------------------------------------------------------------------------------------------------------------------

class AuthorView(generics.ListCreateAPIView, generics.DestroyAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    
    def create(self, request, *args, **kwargs):
        author_data_list = request.data  # Assuming the data sent is a list of author data
        response_data = []
        
        for author_data in author_data_list:
            serializer = self.get_serializer(data=author_data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            response_data.append(serializer.data)
        
        return Response(response_data, status=status.HTTP_201_CREATED)
    
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






def m(request):
    if request.method == 'POST':
        songrank_resource = BookR() 
        dataset = Dataset()
        new_songrank = request.FILES['myfile']
        if not new_songrank.name.endswith('csv'):
            messages.error(request, 'Please upload a CSV file only')
            return render(request, 'upload.html')
        else:
            messages.success(request, 'File successfully uploaded')

        # Read the uploaded CSV file
        data_set = new_songrank.read().decode('utf-8')

        # Create an io.StringIO object to process the CSV data
        io_string = io.StringIO(data_set)

        # Skip the header row
        next(io_string)
        print("yes")
        # Parse CSV data and update/create SongRank objects
        for column in csv.reader(io_string, delimiter=',', quotechar='"'):
            try:
                author, created = Author.objects.get_or_create(name=column[3])
                publisher, created = Publisher.objects.get_or_create(name=column[4])
                category, created = Category.objects.get_or_create(name=column[6])

                

                book, book_created = Book.objects.update_or_create(
                    title=column[1], 
                    subtitle=column[2],
                    expense=column[-1],
                    publishing_date=datetime.datetime.strptime(column[5], '%m/%d/%Y'),
                    defaults={'category': category, 'author': author, 'publisher': publisher}
                )
            except:
                pass

        # Redirect back to the home page
        return render(request, 'upload.html')

    # Render the form page if the request method is not POST
    return render(request, 'upload.html')
