from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('students/', views.students, name='students'),
    path('delete/<int:id>/', views.delete_student, name='delete'),
    path('contact/', views.contact, name='contact'),
]