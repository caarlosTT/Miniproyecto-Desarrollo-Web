from django.shortcuts import render

from .models import LineaFactura
from .models import Factura

# Create your views here.

def factura(request):
    filas = LineaFactura.objects.all()
    datos = Factura.objects.all()

    total = 0
    for dato in datos:
        for fila in filas:
            if dato.id == fila.factura.id:
                total += (fila.precio_unitario * fila.unidades)

    total_iva = total * 1.21


    return render(request, 'factura/factura.html', {
        'filas': filas,
        'total': total,
        'datos': datos,
        'total_iva': total_iva,
    })

def homepage(request):
    return render(request, 'factura/homepage.html')