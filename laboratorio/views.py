from django.shortcuts import render, redirect, get_object_or_404
from .forms import LaboratorioForm
from .models import LaboratorioModel
from django.views.generic import TemplateView
# Create your views here.

class IndexPageView(TemplateView):
    template_name = 'index.html'

def actualizar_view(request,pk):
    datos = LaboratorioModel.objects.get(id=pk)
    #if request.method == 'POST':
    #   return redirect('mostrar')
    context = {'datos': datos}

    return render(request=request, template_name='actualizar.html',context=context)

def actualizar_lab(request,pk):
    nombre = request.POST['nombre']
    ciudad = request.POST['ciudad']
    pais = request.POST['pais']
    datos = LaboratorioModel.objects.get(id=pk)
    datos.nombre = nombre
    datos.ciudad = ciudad
    datos.pais = pais
    datos.save()
    return redirect('/mostrar')

#corregir
def agregar_view(request):
    if request.method == "POST":
        #lab_id = request.POST['id']
        lab_nombre = request.POST['nombre']
        lab_ciudad = request.POST['ciudad']
        lab_pais = request.POST['pais']
        datos = LaboratorioModel(nombre=lab_nombre, ciudad=lab_ciudad, pais= lab_pais)
        datos.save()
        return redirect('mostrar/')
    else:
        return render(request, 'agregar.html')
 

def mostrar_view(request):
    datos = LaboratorioModel.objects.all()
    return render(request,'mostrar.html',{'datos':datos} )


def eliminar_view(request,pk):
    datos = LaboratorioModel.objects.get(id=pk)
    if request.method == 'POST':
        datos.delete()
        return redirect('mostrar')
    context = {'datos': datos,}
    return render(request, 'eliminar.html', context)
