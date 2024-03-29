from django.shortcuts import render, redirect, get_object_or_404
from api.views import Book
from django.utils import timezone
from django.views.generic.list import ListView

from .forms import *
from django.forms import Select


from django.http import HttpResponseRedirect



class BookView(ListView):
    model = Book
    template_name = 'books.html'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Retrieve the queryset of books and assign it to the 'books' key in the context
        context['books'] = self.get_queryset()
        
        return context
    


def retrieveBook(request, id):
    if id:
        try:
            book = Book.objects.get(id=id)
        except Book.DoesNotExist:
            book = None
    else:
        book = None

    return render(request, 'display_book.html', {"book": book})


def FormView(request):
    myfields = ['author', 'category', 'publisher']
    if request.method == "POST":
        form = myf(request.POST)
        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect("/thanks/")
    else:
        form = myf()

    return render(request, 'add_book.html', {'form': form, 'myfields':myfields})



def AddBookForm(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)

        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect("/thanks/")
    else:
        form = AuthorForm()

    return render(request, 'add_author.html', {'form': form})


def AddCategoryForm(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect("/thanks/")
    else:
        form = CategoryForm()

    return render(request, 'add_category.html', {'form': form})



def AddPublisherForm(request):
    if request.method == "POST":
        form = PublisherForm(request.POST)

        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect("/thanks/")
    else:
        form = PublisherForm()

    return render(request, 'add_publisher.html', {'form': form})


def success_page(request):
    return render(request, 'success.html')



def charts(request):
    data = []
    label = []
    query = Book.objects.order_by("title")[:5]
    for ele in query:
        data.append(ele.expense)
        label.append(ele.title)
    return render(request, 'test.html', {"lables":label, "data":data, "query":query})


