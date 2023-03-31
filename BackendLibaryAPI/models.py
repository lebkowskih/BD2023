from django.db import models
from django.contrib.auth.models import AbstractUser

class Author(models.Model):
    name = models.CharField(max_length=100,default='Nie znany')
    surname = models.CharField(max_length=100, default='-')
    birthday = models.DateField()
    nationality = models.CharField(max_length=100)
    author_description = models.TextField()
    # books = models.IntegerField()
    def __str__(self):
        return "%s %s" % (self.name, self.surname)

class Category(models.Model):
    name = models.CharField(max_length=100)
    category_description = models.TextField()
    def __str__(self):
        return "%s" % (self.name)

class Book(models.Model):
    title = models.CharField(max_length = 200)
    isbn = models.IntegerField()
    date_of_publication = models.DateField()
    quantity = models.IntegerField()
    book_description = models.TextField()
    language = models.TextField()
    authors = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class User(AbstractUser):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=50)
    username = None

    USERNAME_FIELD='email'
    REQUIRED_FIELDS = []