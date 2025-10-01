from django.shortcuts import render, redirect
from mainApp.models import Auto, Reserva, Boleta
from mainApp.forms import FormReserva
import datetime

DESCUENTO = 20  

def index(request):
    autos = Auto.objects.all()
    data = {'autos': autos}
    return render(request, 'index.html', data)


def ticket(request, id):
    boleta = Boleta.objects.get(id=id)
    data = {'boleta': boleta}
    return render(request, 'ticket.html', data)


def reservar(request, id):
    form = FormReserva()
    form.fields['id_auto'].initial = id

    if request.method == 'POST':
        form = FormReserva(request.POST)
        if form.is_valid():
            auto = Auto.objects.get(id=id)

            fecha_inicio = form.cleaned_data['fecha_inicio']
            fecha_fin = form.cleaned_data['fecha_fin']
            dias = (fecha_fin - fecha_inicio).days + 1
            if dias < 1:
                dias = 1

            reserva = Reserva()
            reserva.auto = auto
            reserva.cliente_nombre = form.cleaned_data['cliente_nombre']
            reserva.cliente_email = form.cleaned_data['cliente_email']
            reserva.fecha_inicio = fecha_inicio
            reserva.fecha_fin = fecha_fin
            reserva.codigo_descuento = form.cleaned_data['codigo_descuento']
            reserva.save()


            total_original = auto.precio_por_dia * dias
            descuento = DESCUENTO if reserva.codigo_descuento == datetime.date.today().strftime("%Y-%m-%d") else 0
            total_descuento = (total_original * descuento) / 100
            total_final = total_original - total_descuento

            boleta = Boleta()
            boleta.reserva = reserva
            boleta.numero_boleta = f"B-{reserva.id:05d}"
            boleta.fecha_pago = datetime.date.today()
            boleta.total_original = total_original
            boleta.total_descuento = total_descuento
            boleta.total_final = total_final
            boleta.save()

            return redirect('/ticket/' + str(boleta.id))

    auto = Auto.objects.get(id=id)
    data = {
        'auto': auto,
        'form': form
    }
    return render(request, 'reservar.html', data)
