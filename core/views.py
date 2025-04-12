from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Doctor, Appointment, Medicine, Order
from .forms import AppointmentForm, OrderForm

# View to list available doctors
def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'core/doctor_list.html', {'doctors': doctors})

def home(request):
    return render(request, 'core/home.html')

# View to create an appointment
def create_appointment(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)

    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.doctor = doctor
            appointment.save()
            # Redirect to the appointment detail page after booking the appointment
            return redirect('appointment_detail', appointment_id=appointment.id)
    else:
        form = AppointmentForm()

    return render(request, 'core/create_appointment.html', {'form': form, 'doctor': doctor})

# View to list available medicines
def medicine_list(request):
    medicines = Medicine.objects.all()
    return render(request, 'core/medicine_list.html', {'medicines': medicines})

# View to create an order for medicines
def create_order(request, medicine_id):
    medicine = get_object_or_404(Medicine, id=medicine_id)

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.medicine = medicine

            # Make sure the quantity is greater than 0 before placing the order
            if order.quantity <= 0:
                return HttpResponse("Please enter a valid quantity greater than 0.")

            order.total_price = medicine.price * order.quantity
            order.save()
            # Redirect to the order detail page after placing the order
            return redirect('order_detail', order_id=order.id)
    else:
        form = OrderForm()

    return render(request, 'core/create_order.html', {'form': form, 'medicine': medicine})
