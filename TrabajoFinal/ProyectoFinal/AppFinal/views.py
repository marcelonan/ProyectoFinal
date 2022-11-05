from django.http import HttpResponse
from django.shortcuts import render, redirect



# Create your views here.

def inicio(request):
    return render(request, "inicio.html")

def nosotros(request):
    return render(request, "nosotros.html")

def productos(request):
    return render(request, "productos.html")

def tienda(request):
    return render(request, "tienda.html")

def reseña(request):
    
    if request.method == 'POST':
        mi_formulario = reseñas(request.POST)
        print(mi_formulario)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            reseñas = reseña(nombre=data['nombre'], reseña=data['reseña'])
            reseñas.save()
            return redirect('reseña')
    else:
        mi_formulario = reseñas()
    
    
    return render(request, "reseña.html", {'mi_formulario': mi_formulario})