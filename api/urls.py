from django.urls import path, include
from .views import *


urlpatterns = [
    path('book/', BookView.as_view(), name='book'),
    path('author/', AuthorView.as_view(), name='author'),
    path('author/<str:author>/', AuthorViewFind.as_view({'get': 'retrieve'}), name='author-find'),

    path('publisher/', PublisherView.as_view(), name='publisher'),
    path('publisher/<str:publisher>/', PublisherViewFind.as_view({'get': 'retrieve'}), name='author-find'),


    path('category', CategoryView.as_view(), name='category'),
    path('category/<str:category>/', CategoryViewFind.as_view({'get': 'retrieve'}), name='author-find'),

    path('p', m, name="uplaod")


]

