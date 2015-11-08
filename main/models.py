from django.db import models

# Create your models here.

class Content(models.Model):
    date = models.CharField(max_length=200, null=True, blank=True)
    title = models.CharField(max_length=200)
    text = models.TextField()

class Twitter(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()

class Outlet(models.Model):
    title = models.CharField(max_length=200)

class Author(models.Model):
    name = models.CharField(max_length=200)

class Annotation(models.Model):
    rating = models.CharField(max_length=200)

