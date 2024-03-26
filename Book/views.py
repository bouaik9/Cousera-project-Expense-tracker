from django.shortcuts import render
from api.views import Book
from django.utils import timezone
from django.views.generic.list import ListView


# Create your views here.

def fun(request):
    query = Book.objects.all()
    context = {'books': query}  # Create a dictionary with 'query' as the key and the queryset as the value
    print(query[0].title)
    return render(request, 'books.html', context)



class BookView(ListView):
    model = Book
    template_name = 'books.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Retrieve the queryset of books and assign it to the 'books' key in the context
        context['books'] = self.get_queryset()
        
        return context