from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def dashboard(request): # return html for index page
    return render(request, 'index.html')