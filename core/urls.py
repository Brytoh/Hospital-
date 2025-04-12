from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('doctor/<int:doctor_id>/appointment/', views.create_appointment, name='create_appointment'),
    path('medicines/', views.medicine_list, name='medicine_list'),
    path('medicine/<int:medicine_id>/order/', views.create_order, name='create_order'),

    # New URL patterns for appointment and order details
    path('appointment/<int:appointment_id>/', views.appointment_detail, name='appointment_detail'),
    path('order/<int:order_id>/', views.order_detail, name='order_detail'),
]
