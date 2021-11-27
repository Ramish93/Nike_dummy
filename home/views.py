from django.shortcuts import render

# Create your views here.

""" a funciton to render home page"""
def index(request):
    return render(request, 'home/index.html')
    
