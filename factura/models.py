from django.db import models
import datetime

# Create your models here.

class Factura(models.Model):
    id = models.AutoField(primary_key=True)
    num = models.PositiveIntegerField()
    anio = models.PositiveIntegerField()
    fecha_emision = models.DateField()
    cliente_nombre = models.CharField(max_length=100)
    cliente_direccion = models.CharField(max_length=100)

    def lineas(self):
        return LineaFactura.objects.filter(factura=self)

    def total(self):
        total = 0
        for f in self.lineas():
            total += (f.precio_unitario * f.unidades)
        return total

    def total_iva(self):
        return self.total() * 1.21



class LineaFactura(models.Model):
    nombre_producto = models.CharField(max_length=100)
    precio_unitario = models.PositiveIntegerField()
    unidades = models.PositiveIntegerField(default=1)
    factura = models.ForeignKey(
        Factura,
        null=True,
        blank=True,
        on_delete=models.CASCADE, 
        )

    '''He usado el parámetro CASCADE debido a que una factura puede constar 
    de numerosas líneas y por lo tanto, borrar la factura podría ser molesto con PROTECT'''

    def precio_real(self):
        return self.precio_unitario * self.unidades


    

