from django.urls import path
from . import views

#Task23: Create urls to getRoutes, getBooks, and getBooks by id
urlpatterns = [
    path('',  views.getRoutes),
    path('books/', views.getBooks),
    path('books/<str:pk>/', views.getBook),
]
