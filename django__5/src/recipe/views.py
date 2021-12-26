
from django.http import HttpResponse
from django.shortcuts import render
from . import models


# def home_view(request) :
#     print(request.GET.get("q"))
#     print(request.COOKIES)
#     print(request.user)
#     print(request.path)
#     print(request.method)
#     return HttpResponse("hello")

def home_view(request) :
    context = {
        'title':'zehra',
        'dict1' : {'django' : 'best framework'},
        'my_list' : [1,7,3,4,5,],
        'my_list2' : []
        
    }

    return render(request, 'pages/home_page.html', context)
def about_page(request) :
    return HttpResponse('<h2> About_page has shown <h2>')
# Create your views here.
