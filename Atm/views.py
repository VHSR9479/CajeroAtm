from django.http import HttpResponse
from django.template import loader
from models import Banco

def HolaMundo(request):
    bancos = Banco.objects.all()
    contexto = {'bancos':bancos,}
    template = loader.get_template('Cajero/cajero_view.html')
    return HttpResponse(template.render(contexto, request))

def banco(request,idBanco):
    return HttpResponse("Se ha creado el banco %s." % idBanco)