from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required  # Import this decorator
from django.http import HttpResponse
from .models import Doctor, Appointment, Medicine, Order
from .forms import AppointmentForm, OrderForm

# View to list available doctors
def doctor_list(request):
    doctors = Doctor.objects.all()  # Fetch all doctors
    return render(request, 'core/doctor_list.html', {'doctors': doctors})

# Home page view
def home(request):
    return render(request, 'core/home.html')

# View to create an appointment with a specific doctor
@login_required  # This decorator ensures the user must be logged in
def create_appointment(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)

    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.doctor = doctor  # Associate the appointment with the doctor
            appointment.patient = request.user.patient  # Associate the appointment with the logged-in user (if you have a patient-user relation)
            appointment.save()
            # Redirect to the appointment detail page after booking the appointment
            return redirect('appointment_detail', appointment_id=appointment.id)
    else:
        form = AppointmentForm()

    return render(request, 'core/create_appointment.html', {'form': form, 'doctor': doctor})

# View to list available medicines
def medicine_list(request):
    medicines = Medicine.objects.all()  # Fetch all medicines
    return render(request, 'core/medicine_list.html', {'medicines': medicines})

# View to create an order for a specific medicine
def create_order(request, medicine_id):
    medicine = get_object_or_404(Medicine, id=medicine_id)

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.medicine = medicine  # Associate the order with the medicine

            # Make sure the quantity is greater than 0 before placing the order
            if order.quantity <= 0:
                return HttpResponse("Please enter a valid quantity greater than 0.")

            order.total_price = medicine.price * order.quantity  # Calculate total price
            order.save()
            # Redirect to the order detail page after placing the order
            return redirect('order_detail', order_id=order.id)
    else:
        form = OrderForm()

    return render(request, 'core/create_order.html', {'form': form, 'medicine': medicine})

# View for appointment details
def appointment_detail(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)  # Fetch the appointment by ID
    return render(request, 'core/appointment_detail.html', {'appointment': appointment})

# View for order details
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)  # Fetch the order by ID
    return render(request, 'core/order_detail.html', {'order': order})

# View for about page
def about(request):
    return render(request, 'core/about.html')
