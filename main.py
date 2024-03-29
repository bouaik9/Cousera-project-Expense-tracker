import csv
from datetime import datetime

import os
import django

# Set the Django settings module environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project.settings")

# Setup Django
django.setup()
from api.models import Book, Author, Publisher, Category

def add_books_from_csv(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Assuming CSV columns: title, subtitle, publishing_date, expense, author_name, publisher_name, category_name
            # You may need to adjust this based on your actual CSV structure
            
            # Create or get Author object
            print("here")
            author, _ = Author.objects.get_or_create(name=row['authors'])
            
            # Create or get Publisher object
            publisher, _ = Publisher.objects.get_or_create(name=row['publisher'])
            
            # Create or get Category object
            category, _ = Category.objects.get_or_create(name=row['category'])
            
            # Convert string date to datetime object
            publishing_date = datetime.strptime(row['published_date'], '%m/%d/%Y').date()
            
            # Create Book object
            book = Book.objects.create(
                title=row['title'],
                subtitle=row['subtitle'],
                publishing_date=publishing_date,
                expense=float(row['distribution_expense']),
                author=author,
                publisher=publisher,
                category=category
            )
            book.save()

# Usage example:
add_books_from_csv('csv.csv')
