from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    message = '<script>alert("Hello world");</script>'
    return render(request, 'index.html', {'message':message})

def hello(request):
    return HttpResponse("Hello world")