from import_export import resources

from .models import MyBook


class BookR(resources.ModelResource):
    class Meta:
        model = MyBook