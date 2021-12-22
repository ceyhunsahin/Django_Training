from django.urls import path
# from . import views
from .views import home_page

urlpatterns = [
    path('', home_page), # home'un kendisinde gozuksun istiyoruz
]
