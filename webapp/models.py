from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='static/')

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)


