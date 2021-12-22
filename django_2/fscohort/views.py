from django.shortcuts import render
from django.http import HttpResponse


def home_page(request) :
    return HttpResponse('<h2> Hi, this is fscohort home Page <h2>')


# Create your views here.
