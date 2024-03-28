from rest_framework.serializers import ModelSerializer, ValidationError
from .models import Book, Author, Publisher, Category



class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ['name']
    def validate_name(self, value):
        # Check if an author with the same name already exists
        if Author.objects.filter(name=value).exists():
            pass
        return value

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']
    def validate_name(self, value):
        # Check if an author with the same name already exists
        if Author.objects.filter(name=value).exists():
            pass
        return value

class PublisherSerializer(ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['name']

    def validate_name(self, value):
        # Check if an author with the same name already exists
        if Author.objects.filter(name=value).exists():
            pass
        return value
    

class BookSerializer(ModelSerializer):
    author = AuthorSerializer()
    category = CategorySerializer()
    publisher = PublisherSerializer()
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
        category = validated_data.pop('category', None)


        if author_data:
            author, _ = Author.objects.get_or_create(**author_data)
            validated_data['author'] = author

        if publisher_data:
            publisher, _ = Publisher.objects.get_or_create(**publisher_data)
            validated_data['publisher'] = publisher
        if category:
            ccategory, _ = Category.objects.get_or_create(**category)
            validated_data['category'] = ccategory


        book_instance = Book.objects.create(**validated_data)
        return book_instance