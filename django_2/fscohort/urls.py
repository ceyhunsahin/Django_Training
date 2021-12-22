from django.urls import path
# from . import views
from .views import home_page, about_view

urlpatterns = [
    path('', home_page), # home'un kendisinde gozuksun istiyoruz
    path('about/', about_view)
]
