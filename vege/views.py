from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
def receipes(request):
    if request.method == "POST":
        data = request.POST
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')

        Receipe.objects.create(
            receipe_name = receipe_name,
            receipe_description = receipe_description,
            receipe_image = receipe_image
        )
        return redirect('/receipes/')
    
    querySet = Receipe.objects.all() #objects is Manager here by default
    
    if request.GET.get('search'):
        querySet = querySet.filter(receipe_name__icontains = request.GET.get('search'))

    context = {'receipes' : querySet}
    return render(request, 'receipes.html', context)


def update_receipe(request, id):
    querySet = Receipe.objects.get(id = id)

    if request.method == "POST":
        data = request.POST
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')

        querySet.receipe_name = receipe_name
        querySet.receipe_description = receipe_description

        if receipe_image:
            querySet.receipe_image = receipe_image

        querySet.save()
        return redirect('/receipes/')


    context = {'receipe' : querySet}
    return render(request, 'update-receipes.html', context)
    

def delete_receipe(request, id):
    querySet = Receipe.objects.get(id = id)
    querySet.delete()
    return redirect('/receipes/')


