from django.db import models

class Library(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    count_of_books = models.IntegerField()