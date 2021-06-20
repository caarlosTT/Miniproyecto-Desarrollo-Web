from django.contrib import admin
from django.utils.html import format_html

# Register your models here.

from .models import Factura, LineaFactura

class AdminFactura(admin.ModelAdmin):
    list_display = ('anio', 'fecha_emision', 'cliente_nombre', 'cliente_direccion', 'id')

admin.site.register(Factura, AdminFactura)

class AdminLineaFactura(admin.ModelAdmin):
    list_display = ('nombre_producto', 'precio_unitario', 'unidades', 'factura')

admin.site.register(LineaFactura, AdminLineaFactura)
