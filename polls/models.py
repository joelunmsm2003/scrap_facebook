from __future__ import unicode_literals
from django.forms import ModelForm
from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.
# Create your models here.

from django.utils.encoding import python_2_unicode_compatible

import datetime

from django.utils import timezone


from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


# Create your models here.

@python_2_unicode_compatible
class locales(models.Model):
  
    nombre = models.CharField(max_length=300,blank=True)

    def __str__(self):

        return self.nombre


@python_2_unicode_compatible
class plataforma(models.Model):
  
    nombre = models.CharField(max_length=300,blank=True)

    def __str__(self):

        return self.nombre

@python_2_unicode_compatible
class localPlataforma(models.Model):
  
    nomlocal = models.CharField(max_length=300,blank=True)
    nomplat = models.CharField(max_length=300,blank=True)


    def __str__(self):

        return self.nomplat

@python_2_unicode_compatible
class estado(models.Model):
  
    tipo = models.CharField(max_length=300,blank=True)

    def __str__(self):

        return self.tipo


@python_2_unicode_compatible
class tiposicion(models.Model):
  
    tp = models.CharField(max_length=300,blank=True)

    def __str__(self):
        return self.tp




@python_2_unicode_compatible
class personal(models.Model):

    nombre = models.CharField(max_length=300,blank=True)
   

    def __str__(self):
        return self.nombre 


@python_2_unicode_compatible
class interprete(models.Model):

    nombre = models.CharField(max_length=300,null=True,blank=True)
    apellido = models.CharField(max_length=300,blank=True)
    dni = models.CharField(max_length=300,blank=True)
    def __str__(self):

         return self.nombre

@python_2_unicode_compatible
class posicion(models.Model):
  
    idlp = models.ForeignKey(localPlataforma,max_length=300,blank=True)
    tipo = models.ForeignKey(tiposicion,max_length=300,blank=True)
    estadoper= models.ForeignKey(personal,max_length=300,blank=True)
    idInter= models.ForeignKey(interprete,max_length=300,blank=True)
    estado= models.ForeignKey(estado,max_length=300,blank=True)
    
    def __str__(self):
        return self.idlp


@python_2_unicode_compatible
class suplp(models.Model):
  
    idlop = models.ForeignKey(localPlataforma,max_length=300,blank=True)
    nombre = models.CharField(max_length=300,blank=True)
    idloc = models.ForeignKey(locales,max_length=300,blank=True)
    idpl= models.ForeignKey(plataforma,max_length=300,blank=True)
    def __str__(self):
        return self.idlop








