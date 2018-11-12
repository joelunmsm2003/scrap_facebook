from django.shortcuts import render
from app.models import *
from django.views.decorators.csrf import csrf_exempt
import simplejson
from django.http import HttpResponse,JsonResponse
from app.serializers import *
# Create your views here.

from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify

from django.views import View

class PollQuestions(View):
	title = "Questions"
	template = 'questions.html'

	def get(self, request):
		questions = list(Question.objects.values('pk', 'question_text'))

		context = {
			'question_text': self.title,
			'props': questions,
		}

		return render(request, self.template, context)


@receiver(pre_save)
def my_callback(sender, instance, *args, **kwargs):
    
    print sender

    print 'jdjjdjdj',instance



def web(request):

	return render(request, 'web.html',{})

def listausuarios(request):


	_usuarios = Usuarios.objects.all()
	serializer =  UsuariosSerializer(_usuarios,many=True)
	return JsonResponse(serializer.data, safe=False)



def listaglobo(request):


	_data = HistorialGlobo.objects.all()
	serializer =  HistorialGloboSerializer(_data,many=True)
	return JsonResponse(serializer.data, safe=False)



@csrf_exempt
def guarda(request):


	estado= request.GET['estado']
	usuario= request.GET['usuario']

	print 'estado,usuario',estado,usuario


	_user = Usuarios.objects.get(nombre=usuario).id
	_estado= Estado.objects.get(nombre=estado).id

	id_hg= HistorialGlobo.objects.filter(usuario_id=_user).values('id').order_by('-id')[0]['id']

	globo=HistorialGlobo.objects.get(id=id_hg)

	ultimo_estado=globo.estado.nombre

	print '-----',ultimo_estado,estado

	if ultimo_estado==estado:

		print 'Actualizando....',datetime.datetime.today()

		globo.fecha_fin=datetime.datetime.today()
		globo.save()

	else:

		id_hg= HistorialGlobo.objects.filter(usuario_id=_user).values('id').order_by('-id')[0]['id']

		globo=HistorialGlobo.objects.get(id=id_hg)

		globo.fecha_fin=datetime.datetime.today()

		globo.save()

		HistorialGlobo(usuario_id=_user,estado_id=_estado,fecha_inicio=datetime.datetime.today(),fecha_fin=datetime.datetime.today()).save()


	c= simplejson.dumps('ok')

	return HttpResponse(c, content_type="application/json")
