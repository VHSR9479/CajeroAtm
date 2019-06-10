# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Modelo para La base de datos Cajero ( Sistema para emular un modelo de negocio para un cajero de banco )
# Modelo para Banco
class Banco(models.Model):
    id_banco  = models.IntegerField(primary_key=True, unique=True, editable=False)
    nit       = models.CharField(max_length=10)
    nombre    = models.CharField(max_length=45)
    direccion = models.CharField(max_length=45)
    telefono  = models.CharField(max_length=10)

# Modelo para Cajero con referencia a Banco
class Cajero(models.Model):
    id_cajero = models.IntegerField(primary_key=True, unique=True, editable=False)
    id_banco  = models.ForeignKey(Banco, on_delete= models.CASCADE)
    saldo     = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    ubicacion = models.CharField(max_length=45)
    ind_servicio = models.IntegerField()

# Modelo para Estado
class Estado(models.Model):
    id_estado   = models.IntegerField(primary_key=True, unique=True, editable=False)
    descripcion = models.CharField(max_length=45)

# Modelo para Producto
class Producto(models.Model):
    id_producto = models.IntegerField(primary_key=True, unique=True, editable=False)
    descripcion = models.CharField(max_length=45)

# Modelo para Tipo Identificacion
class Tipo_identificacion(models.Model):
    id_identificacion = models.IntegerField(primary_key=True, unique=True, editable=False)
    descripcion       = models.CharField(max_length=45)

# Modelo para usuario con referencia a tipo de usuario
class usuario(models.Model):
    id_usuario     = models.IntegerField(primary_key=True, unique=True, editable=False)
    identificacion = models.CharField(max_length= 15)
    tipo_identificacion = models.ForeignKey(Tipo_identificacion, on_delete= models.CASCADE)
    nombre         = models.CharField(max_length=45)
    apellido       = models.CharField(max_length=45)
    direccion      = models.CharField(max_length=45)
    celular        = models.CharField(max_length=45)
    email          = models.EmailField(max_length=254)
    fecha_creacion = models.DateTimeField('date published')
    fecha_actualizacion = models.DateTimeField('date published')

# Modelo para Cuenta con referencia  a Banco, Producto, Usuario y Estado
class Cuenta(models.Model):
    id_cuenta = models.IntegerField(primary_key=True, unique=True, editable=False)
    numero    = models.CharField(max_length=45)
    id_banco  = models.ForeignKey(Banco, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    id_usuario  = models.ForeignKey(usuario, on_delete=models.CASCADE)
    id_estado   = models.ForeignKey(Estado, on_delete=models.CASCADE)
    saldo       = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    clave       = models.CharField(max_length=45)


# Modelo para Movimiento
class Movimiento(models.Model):
    id_movimiento = models.IntegerField(primary_key=True, unique=True, editable=False)
    descripcion   = models.CharField(max_length=45)


# Modelo para Transaccion  con relacion a cajero
class Transaccion(models.Model):
    id_transaccion = models.IntegerField(primary_key=True, unique=True, editable=False)
    id_cajero      = models.ForeignKey(Cajero, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField('date published')
    ind_estado     = models.ForeignKey(Estado, on_delete=models.CASCADE)
    valor          = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)

# Modelo para  Tarjeta con referencia a cuenta y estado
class Tarjeta(models.Model):
    id_tarjeta   = models.IntegerField(primary_key=True, unique=True, editable=False)
    numero       = models.CharField(max_length=45)
    id_cuenta    = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    id_estado    = models.ForeignKey(Estado, on_delete=models.CASCADE)
    valithru     = models.DateTimeField('date published')
    ind_block    = models.IntegerField()
    clave        = models.CharField(max_length=45)
    fec_creacion = models.DateTimeField('date published')

# Modelo para Detalle con referencia a Transaccion , movimiento, cuenta y tarjeta
class Detalle(models.Model):
    id_detalle      = models.IntegerField(primary_key=True, unique=True, editable=False)
    id_transaccion  = models.ForeignKey(Transaccion, on_delete=models.CASCADE)
    id_movimiento   = models.ForeignKey(Movimiento, on_delete=models.CASCADE)
    id_cuenta       = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    id_tarjeta      = models.ForeignKey(Tarjeta, on_delete=models.CASCADE)
    monto           = models.IntegerField()










