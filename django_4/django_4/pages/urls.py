from django.urls import path
from . import views

urlpatterns = [
    path('', views.page_1),
    path('/x/', views.page_x),
    # path('<int:id>/', views.page_1),
]
