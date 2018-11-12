#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from app.models import *
from django.contrib.admin import RelatedOnlyFieldListFilter

from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
import os.path
import json
import requests
from django.contrib.admin.filters import DateFieldListFilter


@admin.register(Question)
class QuestionGloboAdmin(admin.ModelAdmin):
    list_display = ('id','question_text')



@admin.register(Estado)
class EstadoGloboAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')


@admin.register(Piso)
class PisoAdmin(admin.ModelAdmin):
    list_display = ('id','numero')


@admin.register(Posicion)
class PosicionAdmin(admin.ModelAdmin):
    list_display = ('id','numero','piso')


@admin.register(Ocupacion)
class OcupacionAdmin(admin.ModelAdmin):
    list_display = ('id','placa','numero','estado')
    list_filter=('estado','posicion','placa')




