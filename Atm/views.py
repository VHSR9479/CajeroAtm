from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from models import Banco
from CajeroAtm.views import ruta_vista
from Atm.forms import BancoForm

def bancoView(request):
    bancos = Banco.objects.all()
    ruta = ruta_vista()
    contexto = {'bancos':bancos, 'ruta':ruta.mostrar_ruta(1,"listar Banco"),}
    template = loader.get_template('Banco/banco_view.html')

    return HttpResponse(template.render(contexto, request))

def bancoSave(request,idBanco):
    if request.method == 'POST':
        form = BancoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Atm:formBanco')
    else:
        form = BancoForm

    ruta = ruta_vista()
    template = loader.get_template('Banco/banco_form.html')
    return HttpResponse(template.render({'form':form,'ruta':ruta.mostrar_ruta(1,"Crear Banco"),'tipo':'1'},request))

def bancoEdit(request,idBanco):
    bancos = Banco.objects.filter(id_banco = idBanco);
    if request.method == 'POST':
        form = BancoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Atm:formBanco')
    else:
        form = BancoForm

    ruta = ruta_vista()
    template = loader.get_template('Banco/banco_update.html')
    return HttpResponse(template.render({'form':form,'ruta':ruta.mostrar_ruta(1,"Editar Banco"),'tipo':'1','bancos':bancos},request))


def bancoDelete(request,idBanco):
    bancos = Banco.objects.all()
    ruta = ruta_vista()
    contexto = {'bancos':bancos, 'ruta':ruta.mostrar_ruta(1,"listar Banco"),}
    template = loader.get_template('Banco/banco_view.html')

    return HttpResponse(template.render(contexto, request))