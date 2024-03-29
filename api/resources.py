from import_export import resources

from .models import Book


class BookR(resources.ModelResource):
    class Meta:
        model = Book