from django.contrib import admin

# Register your models here.


#EJEMPLOSSSSSSSSSS......

 
from .models import *
from django.contrib import admin
from django.contrib.admin.filters import RelatedOnlyFieldListFilter

from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy

admin.site.register(Question)


@admin.register(locales)
class localesAdmin(admin.ModelAdmin):

	list_display = ('nombre',)

@admin.register(plataforma)
class plataformaAdmin(admin.ModelAdmin):

	list_display = ('nombre',)

@admin.register(localPlataforma)
class localPlataformaAdmin(admin.ModelAdmin):

	list_display = ('nomlocal','nomplat')

@admin.register(estado)
class estadoAdmin(admin.ModelAdmin):

	list_display = ('tipo',)

@admin.register(posicion)
class posicionAdmin(admin.ModelAdmin):


	list_display = ('idlp','tipo','estadoper','idInter','estado' )


@admin.register(tiposicion)
class tiposicionAdmin(admin.ModelAdmin):


	list_display = ('tp', )

@admin.register(interprete)
class interpreteAdmin(admin.ModelAdmin):
	list_display = ('nombre','apellido','dni')


@admin.register(personal)
class personalAdmin(admin.ModelAdmin):
	list_display = ('nombre',)
	
@admin.register(suplp)
class suplpAdmin(admin.ModelAdmin):
	list_display = ('nombre','idlop','nombre','idloc','idpl')




