from django.urls import path
from . import views 

urlpatterns = [
    path('', views.IndexPageView.as_view(), name='index'),
    path('agregar/', views.agregar_view, name='agregar'),
    path('mostrar/', views.mostrar_view, name='mostrar'),
    path('actualizar/<int:pk>', views.actualizar_view, name='actualizar'),
    path('actualizar/actualizar_lab/<int:pk>', views.actualizar_lab, name='actualizar_lab'),
    path('eliminar/<int:pk>', views.eliminar_view, name='eliminar'),
]