from django.contrib import admin
from .models import Patient, Doctor, Appointment, Medicine, Order

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'specialty', 'email', 'phone', 'image')
    search_fields = ('first_name', 'last_name', 'specialty')

admin.site.register(Patient)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Appointment)
admin.site.register(Medicine)
admin.site.register(Order)
