from __future__ import unicode_literals

from django.db import models
import datetime

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    
class Piso(models.Model):
    numero = models.CharField(max_length=1000)

    class Meta:
        managed = True
        db_table = 'piso'
        verbose_name = 'Piso'

    def __unicode__(self):
        return self.numero


class Posicion(models.Model):
    numero = models.CharField(max_length=1000)
    piso = models.ForeignKey('Piso', models.DO_NOTHING, db_column='piso', blank=True, null=True)
    estado = models.ForeignKey('Estado', models.DO_NOTHING, db_column='estado', blank=True, null=True)
    fecha = models.DateTimeField(blank=True, default=datetime.datetime.today())

    class Meta:
        managed = True
        db_table = 'posicion'
        verbose_name = 'Posicion'

    def __unicode__(self):
        return self.numero

class Ocupacion(models.Model):
    numero = models.CharField(max_length=1000)
    placa = models.CharField(max_length=1000)
    posicion = models.ForeignKey('Posicion', models.DO_NOTHING, db_column='posicion', blank=True, null=True)
    estado = models.ForeignKey('Estado', models.DO_NOTHING, db_column='estado', blank=True, null=True)
    fecha = models.DateTimeField(blank=True, default=datetime.datetime.today())

    class Meta:
        managed = True
        db_table = 'ocupacion'
        verbose_name = 'Ocupacion'

    def __unicode__(self):
        return self.numero


class Estado(models.Model):
    nombre = models.CharField(max_length=1000)

    class Meta:
        managed = True
        db_table = 'estado'
        verbose_name = 'Estado'

    def __unicode__(self):
        return self.nombre

class Usuarios(models.Model):
    nombre = models.CharField(max_length=1000)
    password = models.CharField(max_length=1000)

    class Meta:
        managed = True
        db_table = 'globo'
        verbose_name = 'Usuario'

    def __unicode__(self):
        return self.nombre



class HistorialGlobo(models.Model):
    usuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='usuario', blank=True, null=True)
    estado = models.ForeignKey('Estado', models.DO_NOTHING, db_column='estado', blank=True, null=True)
    fecha = models.DateTimeField(blank=True, default=datetime.datetime.today())
    fecha_inicio = models.DateTimeField(blank=True, default=datetime.datetime.today())
    fecha_fin = models.DateTimeField(blank=True, default=datetime.datetime.today())


    class Meta:
        managed = True
        db_table = 'historial_globo'
        verbose_name = 'Historial Globo'

    def __unicode__(self):
        return self.usuario