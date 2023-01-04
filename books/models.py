from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Task08: Create book model with attributes: title, author, year, rating, and description
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    year = models.PositiveIntegerField(null=True)
    rating = models.PositiveIntegerField(null=True, validators=[MaxValueValidator(10), MinValueValidator(1)])
    description = models.TextField(null=True, blank=True)

    posted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
