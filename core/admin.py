

# Register your models here.

from django.contrib import admin
from .models import Patient, Doctor, Appointment, Medicine, Order

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Medicine)
admin.site.register(Order)


