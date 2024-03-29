from django.contrib import admin
from .models import MyBook
# Register your models here.
from import_export.admin import ImportExportModelAdmin

@admin.register(MyBook)
class BookAdmin(ImportExportModelAdmin):
    list_display = ('title', 'category')