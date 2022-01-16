from django.urls import path
from pages.views import AboutView, IndexView,ContactFormView

urlpatterns = [
    # path('index/', views.index, name = 'index'),
    # path('about/', views.about, name = 'about'),
    path('', IndexView.as_view(), name = 'index'),
    path('about/', AboutView.as_view(), name = 'about'),
    path('contact/', ContactFormView.as_view(), name = 'contact'),
    # path('courses/', views.courses, name = 'courses'),


]