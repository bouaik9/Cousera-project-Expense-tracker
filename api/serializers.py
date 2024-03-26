from rest_framework.serializers import ModelSerializer, ValidationError
from .models import Book, Author, Publisher, Category



class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ['name']
    def validate_name(self, value):
        # Check if an author with the same name already exists
        if Author.objects.filter(name=value).exists():
            raise ValidationError("An author with this name already exists.")
        return value

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']
    def validate_name(self, value):
        # Check if an author with the same name already exists
        if Author.objects.filter(name=value).exists():
            raise ValidationError("An author with this name already exists.")
        return value

class PublisherSerializer(ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['name']

    def validate_name(self, value):
        # Check if an author with the same name already exists
        if Author.objects.filter(name=value).exists():
            raise ValidationError("An author with this name already exists.")
        return value
    

class BookSerializer(ModelSerializer):
    author = AuthorSerializer()
    category = CategorySerializer()
    publisher = PublisherSerializer()
    class Meta:
        model = Book
        exclude = ['id']
    def validate_name(self, value):
        # Check if an author with the same name already exists
        if Author.objects.filter(name=value).exists():
            raise ValidationError("An author with this name already exists.")
        return value
