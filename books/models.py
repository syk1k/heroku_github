# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    class Meta(object):
        """docstring for Meta"""
        ordering = ["-name"]


    def __str__(self):
        return self.name
            


class Author(models.Model):
    situation = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    #headshot = models.ImageField(upload_to="author_headshots")

    def __str__(self):
        return self.name



class BookManager(models.Manager):
    def title_count(self, keyword):
        return self.filter(title__icontains=keyword).count()


class DambeBook(models.Manager):
    def get_queryset(self):
        return super(DambeBook, self).get_queryset().filter(author="Dambe")

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()

    def __str__(self):
        return self.title