from django.urls import path
from . import views 

urlpatterns = [
    path('', views.IndexPageView.as_view(), name='index'),
    path('mostrar', views.mostrar_view, name='mostrar'),
    path('actualizar/<int:pk>', views.actualizar_view, name='actualizar'),
    path('eliminar/<int:pk>', views.eliminar_view, name='eliminar'),
]