from django.db import models
from datetime import datetime

class Book(models.Model):
    bookname = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    count = models.IntegerField()
    def __str__(self):
        return self.bookname
class Borrowed_book(models.Model):
    bookname = models.CharField(max_length=250)
    date = models.DateTimeField(auto_now_add=True)
    