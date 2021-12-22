from django.shortcuts import render
from django.http import HttpResponse


def home_page(request) :
    return HttpResponse('<h2> Hi, this is fscohort home Page <h2>')

def about_view(request) :
    return HttpResponse ('<h2> Hi, this is fscohort about view page<h2>')

# Create your views here.
