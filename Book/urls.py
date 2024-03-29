

from django.urls import path, include
from .views import *


urlpatterns = [

    path('books', BookView.as_view(), name="ayoub"),
    path('book/add', FormView, name='ah'),
    path('book/<int:id>', retrieveBook, name='ah'),
    path('author/add', AddBookForm, name='ash'),
    path('category/add', AddCategoryForm, name='ash'),
    path('publisher/add', AddPublisherForm, name='ash'),
    path('thanks/', success_page, name='ash'),
    path('chart/', charts, name='ash'),





]
