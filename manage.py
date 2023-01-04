#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

'''
@author Sebastian @Date:10/12/22 

'''

# Programmer Notes:
# 1.) Tasks will be defined throughout the program as comments
# Comments will be provided wherever necessary

# How to set up django:
# 1.) python --version | Make sure you have python
# 2.) cd ../foldername/ | Make sure you are in the correct folder to execute the next steps
# 3.) pip install django | installs dijango
# 4.) pip freeze > requirements.txt | Installs all requirements for python or rather updates the requirements file
# 5.) django-admin startproject <foldername> | Creates the main project directory
# 6.) django-admin startapp <foldername> | Creates a base folder that contains some application functionality
# 7.) python manage.py runserver | Runs your server on localhost:8000

# How to make migrations:
# 1.) python manage.py showmigrations | Shows all possible migrations that have been make throughout the project
# 2.) python manage.py sqlmigrate auth 0001_initial | Makes an sql migration to the file named 0001_initial.py
# 3.) python manage.py migrate | Migrates the changes made permanently to the sevrer
    # NOTE: If you are making migrations for the first time in your app you must use, python manage.py migrate APP_NAME
# 4.) python manage.py showmigrations | Check again to see if migrations were actually made, represented as [X] or []
# 5.) python manage.py makemigrations | Will prompt the user with some question to ask in order to update what migrations there are

# Admin commands:
# 1.) python manage.py createsuperuser | Allows for an administrator to control certain aspects of the project

# REST framework commands:
# 1.) pip install djangorestframework --no-cache-dir | Installs the django pip framework

# Task01: Create new Django project called BookStore
# Followed the instructions above.

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
