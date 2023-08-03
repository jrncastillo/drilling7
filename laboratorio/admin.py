from django.contrib import admin
from .models import LaboratorioModel, DirectorGeneralModel, ProductosModel
# Register your models here.

class AdminLab(admin.ModelAdmin):
    readonly_fields = ['id',]
    list_display = ['id','nombre',]

    
class AdminDir(admin.ModelAdmin):
    readonly_fields = ['id',]
    list_display = ['id','nombre','laboratorio',]

class AdminProd(admin.ModelAdmin):
    readonly_fields = ['id',]
    fields = ['nombre','laboratorio','f_fabricacion', 'p_costo', 'p_venta']
    list_display = ['id','nombre','laboratorio','f_fabricacion', 'p_costo', 'p_venta']


admin.site.register(DirectorGeneralModel,AdminDir)
admin.site.register(LaboratorioModel,AdminLab)
admin.site.register(ProductosModel, AdminProd)