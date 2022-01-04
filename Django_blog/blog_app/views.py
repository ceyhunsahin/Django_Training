from django.shortcuts import render


def home_view(request):
    return render(request, 'pages/home_page.html')


# Create your views here.
