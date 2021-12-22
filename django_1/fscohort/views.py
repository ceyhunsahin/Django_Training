from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def first_page(request) :
    return HttpResponse("<h1> Hello World </h1>")
def ilk(request) :
    return HttpResponse('<h3> Ceyhun first page <h3>')