from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.title

class Review(models.Model):
    book = models.ForeignKey(Book)
    reviewer = models.ForeignKey(User)
    review = models.TextField()

    def __unicode__(self):
        return ":".join([self.book.title, self.reviewer.username])
