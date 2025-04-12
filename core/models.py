from django.db import models

# Patient Model
class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    date_of_birth = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name_plural = "Patients"


# Doctor Model
class Doctor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to='doctor_pics/', blank=True, null=True)  # New image field

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name}"

    class Meta:
        verbose_name_plural = "Doctors"


# Appointment Model
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    reason = models.TextField()

    def __str__(self):
        return f"Appointment for {self.patient} with Dr. {self.doctor} on {self.appointment_date.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        verbose_name_plural = "Appointments"
        ordering = ['-appointment_date']


# Medicine Model
class Medicine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Medicines"


# Order Model (For Medicine Purchases)
class Order(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    order_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.total_price = self.medicine.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order for {self.patient} - {self.medicine.name} x{self.quantity}"

    class Meta:
        verbose_name_plural = "Orders"
        ordering = ['-order_date']
