from django import forms
from .models import LaboratorioModel, DirectorGeneralModel, ProductosModel

class LaboratorioForm(forms.ModelForm):
    class Meta:
        model = LaboratorioModel
        fields = ["nombre"]

class DirectorForm(forms.ModelForm):
    class Meta:
        model = DirectorGeneralModel
        fields = ["nombre"]

class ProductosForm(forms.ModelForm):
    class Meta:
        model = ProductosModel
        fields = ["nombre",'f_fabricacion', 'p_costo', 'p_venta']