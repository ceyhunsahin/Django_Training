
from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from .forms import StudentForm
from .models import Student


# def home_view(request) :
#     print(request.GET.get("q"))
#     print(request.COOKIES)
#     print(request.user)
#     print(request.path)
#     print(request.method)
#     return HttpResponse("hello")

def home_view(request) :
    # form = StudentForm()
    # context = {
    #     'title':'zehra',
    #     'dict1' : {'django' : 'best framework'},
    #     'my_list' : [1,7,3,4,5,],
    #     'my_list2' : [],
    #     'form' : form
    #
    #
    # }

    return render(request, 'pages/home_page.html')

def student_list(request):
    students = Student.objects.all()
    context = {
        'students' : students,
        'counts' : students.count()
    }

    return render(request, 'pages/student_list.html', context)

def student_add(request):
    form = StudentForm()
    print(request.POST)
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid() :
            form.save()
            return redirect('add')

    context = {
        'form' : form

    }
    return render(request,'pages/student_add.html', context)

def student_detail(request, id):
    student = Student.objects.get(id = id)
    context = {
        'student' : student
    }
    return render(request, 'pages/student_detail.html', context)


def student_delete(request, id):
    student = get_object_or_404(Student, id = id)
    if request.method == 'POST':
        student.delete()
        return redirect('list')
    return render(request, 'pages/student_delete.html')


def student_update(request, id) :
    obj = get_object_or_404(Student, id = id)
    form = StudentForm(instance = obj)
    if request.method == 'POST' :
        form = StudentForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('list')
    context = {
        "student" : obj,
        "form" : form
    }
    return render(request, "pages/student_update.html", context)


def student_updated(request, id):
    student = Student.objects.get(id = id)
    context = {
        'student': student,
    }
    return render(request, 'pages/student_updated.html', context)
# Create your views here.
