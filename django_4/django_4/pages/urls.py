from django.urls import path
from . import views

urlpatterns = [
    path('', views.page_1),
    path('x/', views.page_x),
    path('send_to_this_url/', views.page_x),
    path('add/', views.student_add, name='student_add'),
    # path('<int:id>/', views.page_1),
]
