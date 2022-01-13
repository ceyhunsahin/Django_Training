from django.urls import path
# from . import views
from pages.views import AboutView, IndexView

urlpatterns = [
    # path('index/', views.index, name = 'index'),
    # path('about/', views.about, name = 'about'),
    path('', IndexView.as_view(), name = 'index'),
    path('about/', AboutView.as_view(), name = 'about'),
    # path('courses/', views.courses, name = 'courses'),


]