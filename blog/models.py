#
#  FILE		      : models.py
#  PROJECT		  : Django-blog
#  PROGRAMMER	  : Victor Barbosa
#  FIRST VERSION  : 2022-07-01
#  DESCRIPTION	  : This file contains the models for the blog app.
#


import email
from django.db.models import CASCADE
from django.db import models


# Author model
class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    adress = models.CharField(max_length=50)

    def full_name(self):
        return f"{self.first_name} {self.last_name} "

    def __str__(self):
        return self.full_name()


# Tag model
class Tag(models.Model):
    name = models.SlugField(max_length=50)

    # object name (used in the admin panel)
    def __str__(self):
        return self.name


# Post model
class Post(models.Model):
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    title = models.CharField(max_length=50)
    date = models.DateTimeField()
    image = models.ImageField(
        upload_to="images", height_field=None, width_field=None, max_length=100)
    excerpt = models.CharField(max_length=150)
    tag = models.ManyToManyField(Tag, blank=True, db_index=True)
    content = models.TextField()
    slug = models.SlugField(unique=True, db_index=True)

    # object name (used in the admin panel)
    def __str__(self):
        return f"{self.title} -- {self.date}"


# Commentary model
class Commentary(models.Model):
    author = models.CharField(max_length=20)
    date = models.DateField(auto_now_add=True)
    content = models.TextField(max_length=150)
    post = models.ForeignKey(
        Post, on_delete=models.SET_NULL, null=True, related_name="comments")

    # object name (used in the admin panel)
    def __str__(self):
        return f"{self.author}: {self.content} ({self.date})"
