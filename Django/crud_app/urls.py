from django.urls import path
from crud_app import views


urlpatterns = [
    path('', views.employee, name='employee'),  
    path('list', views.employee_list, name='employee_list'),
]