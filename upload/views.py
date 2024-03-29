from django.shortcuts import render
from tablib import Dataset
from .resources import BookR  # Assuming BookR is defined in resources.py within the same app
from .models import MyBook, Categ  # Assuming you have a model named SongRank defined in models.py
from django.contrib import messages
import io
import csv

def m(request):
    if request.method == 'POST':
        songrank_resource = BookR() 
        dataset = Dataset()
        new_songrank = request.FILES['myfile']
        if not new_songrank.name.endswith('csv'):
            messages.error(request, 'Please upload a CSV file only')
            return render(request, 'upload.html')
        else:
            messages.success(request, 'File successfully uploaded')

        # Read the uploaded CSV file
        data_set = new_songrank.read().decode('utf-8')

        # Create an io.StringIO object to process the CSV data
        io_string = io.StringIO(data_set)

        # Skip the header row
        next(io_string)

        # Parse CSV data and update/create SongRank objects
        for column in csv.reader(io_string, delimiter=',', quotechar='"'):
            category, created = Categ.objects.get_or_create(name=column[3])
            book, book_created = MyBook.objects.update_or_create(
                title=column[1], 
                defaults={'category': category}
            )

        # Redirect back to the home page
        return render(request, 'upload.html')

    # Render the form page if the request method is not POST
    return render(request, 'upload.html')
