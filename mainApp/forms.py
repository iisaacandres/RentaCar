from django import forms

class FormReserva(forms.Form):
    id_auto = forms.CharField(widget=forms.HiddenInput)
    cliente_nombre = forms.CharField()
    cliente_email = forms.CharField(required=False)
    fecha_inicio = forms.DateField(widget=forms.SelectDateWidget)
    fecha_fin = forms.DateField(widget=forms.SelectDateWidget)
    codigo_descuento = forms.CharField(required=False)

    id_auto.widget.attrs['class'] = 'form-control'
    cliente_nombre.widget.attrs['class'] = 'form-control'
    cliente_email.widget.attrs['class'] = 'form-control'
    fecha_inicio.widget.attrs['class'] = 'form-control'
    fecha_fin.widget.attrs['class'] = 'form-control'
    codigo_descuento.widget.attrs['class'] = 'form-control'
