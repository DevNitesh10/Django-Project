from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    # return HttpResponse("Hello, Sabin! You're at the polls index.")
    return render(request,"crud/index.html")

def about(request):
    return render(request,"crud/about.html")