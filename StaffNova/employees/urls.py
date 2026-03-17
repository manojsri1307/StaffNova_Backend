from django.urls import path
from .views import RegisterView, EmployeeListCreateView, EmployeeDetailView

urlpatterns = [
    path('register/', RegisterView.as_view(), name="Register_user"),
    path('employees/', EmployeeListCreateView.as_view(), name='EmployeeListCreateView'),
    path('employees/<int:id>/', EmployeeDetailView.as_view(), name='EmployeeDetailView'),
]