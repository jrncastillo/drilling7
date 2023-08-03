from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import LaboratorioForm
from .models import LaboratorioModel
from django.views.generic import TemplateView
# Create your views here.

class IndexPageView(TemplateView):
    template_name = 'mostrar.html'

def agregar_view(request):
    if request.method == "POST":
        lab_nombre = request.POST['nombre']
        lab_ciudad = request.POST['ciudad']
        lab_pais = request.POST['pais']
        datos = LaboratorioModel(nombre=lab_nombre,ciudad=lab_ciudad,pais= lab_pais)
        datos.save()
        return redirect('mostrar')
    else:
        return render(request, 'agregar.html')


def mostrar_view(request):
    datos = LaboratorioModel.objects.all()
    return render(request,'mostrar.html',{'datos':datos} )
    

def actualizar_view(request):
    lab_id = request.POST['id']
    lab_nombre = request.POST['nombre']
    lab_ciudad = request.POST['ciudad']
    lab_pais = request.POST['pais']
    datos = LaboratorioModel.objects.get(id=lab_id)
    datos.nombre = lab_nombre
    datos.ciudad = lab_ciudad
    datos.pais = lab_pais
    datos.save()
    return redirect('mostrar')


def eliminar_view(request,pk):
    datos = LaboratorioForm.objects.get(id=pk)
    if request.method == 'POST':
        datos.delete()
        return redirect('mostrar')
    context = {'datos': datos,}
    return render(request, 'eliminar.html', context)
