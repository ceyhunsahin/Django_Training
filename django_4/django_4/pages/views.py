
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

def page_1(request):
    names = ['ceyhun', 'zehra', 'Alperen', 'Volkan', 'sevil']
    # return HttpResponse(f'Ceyhun sahin ')
    return render(request, 'local_pages/page_2.html',{'names' : names})
def page_x(request):
    names = ['ceyhun', 'zehra', 'Alperen', 'Volkan', 'sevil']
    # return HttpResponse(f'Ceyhun sahin ')
    return render(request, 'local_pages/page_3.html',{'names' : names})
# Create your views here.
