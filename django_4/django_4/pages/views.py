
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from .forms import StudentForm 

def page_1(request):
    names = ['ceyhun', 'zehra', 'Alperen', 'Volkan', 'sevil']
    # return HttpResponse(f'Ceyhun sahin ')
    return render(request, 'local_pages/page_2.html',{'names' : names})
def page_x(request):
    names = ['ceyhun', 'zehra', 'Alperen', 'Volkan', 'sevil']
    # return HttpResponse(f'Ceyhun sahin ')
    return render(request, 'local_pages/page_3.html',{'names' : names})

def student_add(request):
    form = StudentForm()
    html = 'Welcome'
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            html = "Student succesfully added"

    context = {
        'form': form,
        'html': html
    }
    return render(request, 'local_pages/student_add.html', context)
# Create your views here.
