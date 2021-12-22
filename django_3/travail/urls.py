
from django.urls import path
from . import views

app_name = 'ali'

urlpatterns = [
    path ('', views.snippet_list),
    path ('<int:id>/', views.snippet_detail, name = 'detail'),
    path ('<int:id>/', views.snippet_detail, name = 'number')
]
