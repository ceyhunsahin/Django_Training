from django.shortcuts import render
from django.http import HttpResponse
from .models import Course, Category, Tag

def course_list(request):
    # courses = Course.objects.get (category__slug=slug)
    courses = Course.objects.all().order_by('-date')

    categories = Category.objects.all()
    tags= Tag.objects.all()
    context = {
        'courses' : courses,
        # 'courses': courses,
        'categories': categories,
        'tags':tags
    }
    return render(request, 'courses.html', context)


def course_detail(request, category_slug, course_id):
    # current_user = request.user
    course = Course.objects.get(category__slug=category_slug, id = course_id)
    print(type(course))
    categories = Category.objects.all()
    tags = Tag.objects.all()
    # if current_user.is_authenticated:
    #     enrolled_courses = current_user.courses_joined.all()
    #
    # else:
    #     enrolled_courses = courses

    #enrolled_courses = current_user.courses_joined.all()

    context = {
        'course': course,
        # 'enrolled_courses': enrolled_courses,
        'categories': categories,
        'tags': tags
    }

    return render(request, 'course.html', context)

def category_list(request, category_slug):
    courses = Course.objects.all().filter(category__slug=category_slug)


    categories = Category.objects.all()
    tags= Tag.objects.all()
    context = {
        'courses': courses,
        'categories': categories,
        'tags':tags
    }
    return render(request, 'courses.html', context)

def tag_list(request, tag_slug):
    courses = Course.objects.all().filter(tags__slug = tag_slug)
    categories = Category.objects.all ()
    tags = Tag.objects.all()
    context = {
        'courses' : courses,
        'categories': categories,
        'tags': tags
    }
    return render(request, 'courses.html', context)