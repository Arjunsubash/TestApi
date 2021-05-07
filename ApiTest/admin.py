from django.contrib import admin
from .models import (Book,Borrowed_book)

admin.site.register(Book)
admin.site.register(Borrowed_book)