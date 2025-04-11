from django import forms
from .models import Appointment, Order

# Appointment form
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient', 'doctor', 'appointment_date', 'reason']  # Added doctor field

# Order form
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['patient', 'medicine', 'quantity']  # Added medicine field
