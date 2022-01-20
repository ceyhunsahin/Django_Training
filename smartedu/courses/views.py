from django.http import HttpResponse, HttpResponseRedirect
from .models import Course, Category, Tag,Teacher
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.db.models import Q

def course_list(request, category_slug = None, tag_slug = None):
    category_page = None
    tag_page = None
    categories = Category.objects.all()
    tags = Tag.objects.all()
    current_user = request.user
    ceyhun = Course.objects.all()
    ceyhun = ceyhun.te
    print ('ceyhun', ceyhun)
    if category_slug != None:
        category_page = get_object_or_404(Category, slug = category_slug)
        courses = Course.objects.filter(available=True, category= category_page)
    elif tag_slug != None :
        tag_page = get_object_or_404(Tag, slug = tag_slug)
        courses = Course.objects.filter(available=True, tags= tag_page)

    else:
        if current_user.is_authenticated :
            enrolled_course = current_user.courses_joined.all()
            courses = Course.objects.all ().order_by ('-date')

            for course in enrolled_course :
                courses = courses.exclude(id = course.id)
                print('courses', courses)
        else:
            courses = Course.objects.all ().order_by ('-date')


    context = {
        'courses' : courses,
        'categories': categories,
        'tags':tags
        }
    return render(request, 'courses.html', context)






def course_detail(request, category_slug, course_id):
    current_user = request.user
    print(current_user)
    course = Course.objects.get(category__slug=category_slug, id = course_id)
    courses = Course.objects.all ().order_by ('-date')
    categories = Category.objects.all()
    tags = Tag.objects.all()
    if current_user.is_authenticated:
        enrolled_courses = current_user.courses_joined.all()

    else:
        enrolled_courses = courses

    context = {
        'course': course,
        'enrolled_courses' : enrolled_courses,
        'categories': categories,
        'tags': tags

    }

    return render(request, 'course.html', context)
    # print(HttpResponseRedirect(reverse('course_detail', args=(category_slug, course_id))))
    # return HttpResponseRedirect(reverse('course_detail', args=(category_slug, course_id)))

def search(request) :
    # courses = Course.objects.all().filter (name__contains = request.GET['search'])
    courses = Course.objects.filter(
        Q(name__icontains=request.GET['search']) | Q(teacher__name__icontains=request.GET['search'])
    )
    categories = Category.objects.all()
    tags = Tag.objects.all()
    context = {
        'courses': courses,
        'categories': categories,
        'tags': tags
    }
    return render(request, 'courses.html', context)





# def course_list(request):
#     # courses = Course.objects.get (category__slug=slug)
#     courses = Course.objects.all().order_by('-date')
#
#     categories = Category.objects.all()
#     tags= Tag.objects.all()
#     context = {
#         'courses' : courses,
#         # 'courses': courses,
#         'categories': categories,
#         'tags':tags
#     }
#     return render(request, 'courses.html', context)
# def category_list(request, category_slug):
#     courses = Course.objects.all().filter(category__slug=category_slug)
#
#
#     categories = Category.objects.all()
#     tags= Tag.objects.all()
#     context = {
#         'courses': courses,
#         'categories': categories,
#         'tags':tags
#     }
#     return render(request, 'courses.html', context)
#
# def tag_list(request, tag_slug):
#     courses = Course.objects.all().filter(tags__slug = tag_slug)
#     categories = Category.objects.all ()
#     tags = Tag.objects.all()
#     context = {
#         'courses' : courses,
#         'categories': categories,
#         'tags': tags
#     }
#     return render(request, 'courses.html', context)