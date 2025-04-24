from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tienda/', views.tienda, name='tienda'),
    path('quienes_somos/', views.quienes_somos, name='quienes_somos'),
    path('detalles/', views.detalles, name='detalles'),
]