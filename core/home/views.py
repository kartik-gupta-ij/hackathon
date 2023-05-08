from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def home(request):

    peoples=[
        {'name':'John', 'age': 23}, 
        {'name':'Jhne', 'age': 3},
        {'name':'Jgne', 'age': 2433},
        {'name':'Jne', 'age': 6},
        {'name':'Jane', 'age': 23},
    ]

    return render(request, 'home/index.html' ,context={'peoples':peoples, 'page':'home'})

def about(request):
    context={'page':'about'}
    return render(request, 'home/about.html', context)

def contact(request):
    context={'page':'contact'}
    return render(request, 'home/contact.html', context)