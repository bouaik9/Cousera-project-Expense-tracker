from rest_framework.serializers import ModelSerializer, ValidationError
from .models import Book, Author, Publisher, Category

class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"
    def validate_name(self, value):
        # Check if an author with the same name already exists
        if Author.objects.filter(name=value).exists():
            raise ValidationError("An author with this name already exists.")
        return value

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class PublisherSerializer(ModelSerializer):
    class Meta:
        model = Publisher
        fields = "__all__"

    def validate_name(self, value):
        # Check if an author with the same name already exists
        if Author.objects.filter(name=value).exists():
            raise ValidationError("An author with this name already exists.")
        return value
