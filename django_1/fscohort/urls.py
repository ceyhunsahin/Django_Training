from django.urls import path
from . import views

urlpatterns = [
    path('', views.first_page), # home4un kendisinde gozuksun istiyoruz
    path('ilk/', views.ilk, name = '1.sayfa') # home/home/ page4de ic ice olusturuyoruz
]
