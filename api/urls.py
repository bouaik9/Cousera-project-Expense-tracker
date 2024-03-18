from django.urls import path, include
from .views import *


urlpatterns = [
    path('book/', BookView.as_view(), name='book'),
    path('author/', AuthorView.as_view(), name='author'),
    path('publisher/', PublisherView.as_view(), name='publisher'),
    path('category/', CategoryView.as_view(), name='category'),

]
