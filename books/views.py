# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView
from books.models import Publisher


# Create your views here.

class PublisherList(ListView):
	#model = Publisher
	context_object_name = "publishers"
	queryset = Publisher.objects.all()
