from django.http import HttpResponse
from django.shortcuts import render
from .models import Blog #Objects is Manager here by default

# Create your views here.
def index(request):
    blog = Blog.objects.all()
    return render(request,"crud/index.html", {"blogs" : blog})

def about(request):
    return render(request,"crud/about.html")