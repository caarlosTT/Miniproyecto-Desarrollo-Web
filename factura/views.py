from django.shortcuts import render

from .models import LineaFactura
from .models import Factura

# Create your views here.

def factura(request):
    facturas = Factura.objects.all()

    return render(request, 'factura/factura.html', {
        'facturas': facturas,
    })

def homepage(request):
    return render(request, 'factura/homepage.html')

def detalle(request, pk):
    factura = Factura.objects.get(id=pk)
    return render(request, 'factura/detalle.html', {
        'factura': factura,
    })