from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=1000)
    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=1000)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=1000)
    subtitle = models.CharField(max_length=1000)

    publishing_date = models.DateField()
    expense = models.FloatField(default=0.0)  # Assuming 0.0 as default value
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
