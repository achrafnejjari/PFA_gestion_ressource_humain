from django.urls import path 
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),  # http://127.0.0.1:8000/pages/index/
    path('list_employees/', views.list_employees, name='list_employees'),

]