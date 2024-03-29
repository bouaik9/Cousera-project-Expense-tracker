from django.db import models

# Create your models here.
from django.db import models

class Categ(models.Model):
    name = models.CharField(max_length=500, unique=True)

class MyBook(models.Model):
    title = models.CharField(max_length=500)
    category = models.ForeignKey(Categ, on_delete=models.CASCADE)
