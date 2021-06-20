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

class LineaFactura(models.Model):
    nombre_producto = models.CharField(max_length=100)
    precio_unitario = models.PositiveIntegerField()
    unidades = models.PositiveIntegerField(default=1)
    factura = models.ForeignKey(
        Factura,
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        )
    
    def precio_real(self):
        return self.precio_unitario * self.unidades


    

