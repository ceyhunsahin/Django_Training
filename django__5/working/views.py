from django.shortcuts import render
from django.http import JsonResponse
from recipe.models import Student
from django.core.serializers import serialize

# Create your views here.
def home_api(request):
    data = {
        'name' : 'ceyhun',
        'address' :'clarusway.com',
        'skills' : ['python', 'django']

    }
    return JsonResponse(data)

# def student_list_api(request):
#     if request.method == 'GET' :
#         students = Student.objects.all()
#         student_count = Student.objects.count()
#         student_list = []
#         for student in students:
#             student_list.append({
#                 'first_name' : student.first_name,
#                 'last_name' : student.last_name,
#                 'number' : student.number
#             })
#
#         data = {
#             'students' : student_list,
#             'student_count' : student_count
#             }
#         return JsonResponse(data)

def student_list_api(request):
    if request.method == 'GET':
        students = Student.objects.all ()
        student_count = Student.objects.count()
        student_data = serialize('python',students)
        print(student_data)

        data = {
                     'students' : student_data,
                     'student_count' : student_count
                     }
        return JsonResponse(data)