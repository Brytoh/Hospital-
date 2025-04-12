from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('appointment/<int:doctor_id>/', views.create_appointment, name='create_appointment'),
    path('appointment-detail/<int:appointment_id>/', views.appointment_detail, name='appointment_detail'),
    path('medicines/', views.medicine_list, name='medicine_list'),
    path('order/<int:medicine_id>/', views.create_order, name='create_order'),
    path('order-detail/<int:order_id>/', views.order_detail, name='order_detail'),
    path('about/', views.about, name='about'),  # ✅ New About page route
]
