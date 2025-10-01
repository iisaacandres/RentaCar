from django.db import models
from django.utils import timezone



class Auto(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    anio = models.PositiveIntegerField()
    patente = models.CharField(max_length=10, unique=True)
    precio_por_dia = models.PositiveBigIntegerField()
    color = models.CharField(max_length=30)
    imagen = models.ImageField(upload_to="autos")

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.anio}) - {self.patente}"


class Reserva(models.Model):
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    cliente_nombre = models.CharField(max_length=100)
    cliente_email = models.CharField(max_length=100, blank=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    codigo_descuento = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"Reserva {self.id} - {self.cliente_nombre}"


class Boleta(models.Model):
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    numero_boleta = models.CharField(max_length=30, unique=True)
    fecha_pago = models.DateField(default=timezone.localdate)
    total_original = models.PositiveBigIntegerField(default=0)
    total_descuento = models.PositiveBigIntegerField(default=0)
    total_final = models.PositiveBigIntegerField(default=0)

   
