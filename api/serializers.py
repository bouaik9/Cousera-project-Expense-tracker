from rest_framework.serializers import ModelSerializer, ValidationError, CharField
from rest_framework.validators import UniqueValidator

from .models import Book, Author, Publisher, Category



class AuthorSerializer(ModelSerializer):
    name = CharField(validators=[
        UniqueValidator(queryset=Author.objects.all(), message="An author with this name already exists.")
    ])
    class Meta:
        model = Author
        fields = ['name']
  

class CategorySerializer(ModelSerializer):
    name = CharField(validators=[
        UniqueValidator(queryset=Category.objects.all(), message="An category with this name already exists.")
    ])
    class Meta:
        model = Category
        fields = ['name']
  
class PublisherSerializer(ModelSerializer):
    name = CharField(validators=[
        UniqueValidator(queryset=Publisher.objects.all(), message="An p with this name already exists.")
    ])
    class Meta:
        model = Publisher
        fields = ['name']

 

class BookSerializer(ModelSerializer):
    category = CategorySerializer()
    
    class Meta:
        model = Book
        fields = ['title', 'subtitle', 'author', 'category', 'publisher', 'publishing_date', 'expense']  # Include 'name' field
    
    def validate_title(self, value):
        if Book.objects.filter(title=value).exists():
            raise ValidationError("A Book with this name already exists.")
        return value

    def create(self, validated_data):
        author_data = validated_data.pop('author', None)
        publisher_data = validated_data.pop('publisher', None)
        category_data = validated_data.pop('category', None)
        print(validated_data)
        if author_data:
            author, _ = Author.objects.get_or_create(name=author_data['name'])
            validated_data['author'] = author.id

        if publisher_data:
            publisher, _ = Publisher.objects.get_or_create(name=publisher_data['name'])
            validated_data['publisher'] = publisher.id

        if category_data:
            category, _ = Category.objects.get_or_create(name=category_data['name'])
            validated_data['category'] = category.id
        
        book_instance = Book.objects.create(**validated_data)
        return book_instance