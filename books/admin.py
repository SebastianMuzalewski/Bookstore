from django.contrib import admin

# Import models in current application folder
from .models import Book

# Task11: Register book in model admin
admin.site.register(Book)

