from django.db import models

# Create your models here.
class LaboratorioModel(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50,)
    ciudad = models.CharField(max_length=50,default="-")
    pais = models.CharField(max_length=50,default="-")

class DirectorGeneralModel(models.Model):
    nombre = models.CharField(max_length=50,)
    laboratorio = models.OneToOneField(LaboratorioModel, on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=50,default="-")

class ProductosModel(models.Model):
    nombre = models.CharField(max_length=50,)
    laboratorio= models.ForeignKey(LaboratorioModel, on_delete=models.CASCADE, related_name='productos',)
    f_fabricacion = models.DateField(auto_now_add=False,default='2015',) #revisar
    p_costo = models.DecimalField(max_digits=12, decimal_places=2,)
    p_venta = models.DecimalField(max_digits=12, decimal_places=2,) 




