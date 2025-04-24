from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def tienda(request):
    return render(request, 'tienda.html')

def quienes_somos(request):
    return render(request, 'quienes_somos.html')

def detalles(request):
    return render(request, 'detalles.html')
