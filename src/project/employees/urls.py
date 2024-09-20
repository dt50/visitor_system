from django.urls import path
from .views import EmployeeListView, EmployeeCreateView

app_name = 'employees'

urlpatterns = [
    path('', EmployeeListView.as_view(), name='employees_list'),
    path('create/', EmployeeCreateView.as_view(), name='employee_create'),
]