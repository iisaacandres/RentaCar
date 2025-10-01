from django.contrib import admin
from mainApp.models import Auto, Reserva, Boleta

class AutoAdmin(admin.ModelAdmin):
    list_display = ['marca', 'modelo', 'anio', 'patente', 'precio_por_dia', 'color']

class ReservaAdmin(admin.ModelAdmin):
    list_display = ['auto', 'cliente_nombre', 'cliente_email', 'fecha_inicio', 'fecha_fin', 'codigo_descuento']

class BoletaAdmin(admin.ModelAdmin):
    list_display = ['numero_boleta', 'reserva', 'fecha_pago', 'total_original', 'total_descuento', 'total_final']


admin.site.register(Auto, AutoAdmin)
admin.site.register(Reserva, ReservaAdmin)
admin.site.register(Boleta, BoletaAdmin)
