from django.shortcuts import render
from app.models import *
from django.views.decorators.csrf import csrf_exempt
import simplejson
from django.http import HttpResponse,JsonResponse
# Create your views here.


@csrf_exempt
def guarda(request):


	estado= request.GET['estado']
	usuario= request.GET['usuario']

	id_hg= HistorialGlobo.objects.all().values('id')[0]['id']

	globo=HistorialGlobo.objects.get(id=id_hg)

	ultimo_estado=globo.estado.nombre

	if ultimo_estado==estado:

		print 'Actualizando....'

		globo.fecha_fin=datetime.datetime.today()

	else:

		HistorialGlobo(usuario_id=_user,estado_id=_estado).save()

	_user = Usuarios.objects.get(nombre=usuario).id
	_estado= Estado.objects.get(nombre=estado).id

	HistorialGlobo(usuario_id=_user,estado_id=_estado).save()

	c= simplejson.dumps('ok')

	return HttpResponse(c, content_type="application/json")
