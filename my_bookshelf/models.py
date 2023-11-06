from django.db import models


class Bookshelf(models.Model):
    title= models.CharField(max_length=20,default='')
    author=models.CharField(max_length=20, default='')
    isbn=models.CharField(max_length=30, default='')
    summary=models.TextField(max_length=100, default='')
    genre=models.CharField(max_length=20,default='')
    publish_date=models.DateTimeField(auto_now=True)

