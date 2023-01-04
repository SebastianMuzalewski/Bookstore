from django.urls import path
# Import views from current base app folder
from . import views

# Create base app urls
urlpatterns = [
    # Route for login page
    path('login/', views.loginPage, name="login"),
    # Route for login page
    path('logout/', views.logoutUser, name="logout"),
    # Route for register page
    path('register/', views.registerUser, name="register"),

    # Add path to route to books page view function
    path('', views.books, name="books"),

    # Add path to route to book page view function
    # Use id passed in url to get book
    path('book/<str:pk>/', views.book, name="book"),

    # Route to add book using form
    path('add_book/', views.addBook, name="add_book"),
    # Route to edit book using form
    path('update_book/<str:pk>/', views.updateBook, name="update_book"),
    # Route to delete book
    path('delete_book/<str:pk>/', views.deleteBook, name="delete_book"),
]