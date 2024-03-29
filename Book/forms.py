from django import forms

from api.models import Author, Book, Category, Publisher


class myff(forms.Form):
    title = forms.CharField(label='Title')
    publisher = forms.ChoiceField(label='Publisher', choices=[('ayoub', 'ayoub')] * 3)
    publication_date = forms.DateField(label='Published Date', widget=forms.DateInput(attrs={'type': 'date'}))
    category = forms.ChoiceField(label='Category', choices=[('ayoub', 'ayoub')] * 3)
    distribution_expense = forms.CharField(label='Distribution Expense')

class myf(forms.ModelForm):
    publishing_date = forms.DateField(label='Published Date', widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Book
        fields = '__all__'


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name']
        
        
