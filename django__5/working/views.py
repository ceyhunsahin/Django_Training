from django.shortcuts import render
from django.http import JsonResponse
from recipe.models import Student
from django.core.serializers import serialize
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import StudentSerializer
from rest_framework import status

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

# def student_list_api(request):
#     if request.method == 'GET':
#         students = Student.objects.all ()
#         student_count = Student.objects.count()
#         student_data = serialize('python',students)
#         print(student_data)
#         print ('ceyhun')
#         data = {
#                      'students' : student_data,
#                      'student_count' : student_count
#                      }
#         return JsonResponse(data)
# @csrf_exempt
# def student_create_api(request):
#     if request.method == 'POST':
#         post_body = json.loads(request.body)
#         print(post_body)
#         firstname = post_body.get('first_name')
#         lastname = post_body.get('last_name')
#         number = post_body.get('number')
#         student_data = {
#             'first_name' : firstname,
#             'last_name' : lastname,
#             'number' : number
#         }
#         #print(**student_data)
#         student_obj = Student.objects.create(**student_data) # data unpacked
#         data = {
#             'message' : f'Student {student_obj.first_name} created successfully '
#         }
#         return JsonResponse(data, status=201)

@api_view(['GET', 'POST'])
def student_list_create_api(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many = True)
        return Response(serializer.data)
    if request.method == 'POST' :
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'message' : 'Student created successfully'

            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)