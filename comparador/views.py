from django.shortcuts import render, get_object_or_404
from .models import Procesador

def seleccion_procesadores(request):
    procesadores = Procesador.objects.all()
    return render(request, 'seleccion.html', {'procesadores': procesadores})

def comparar_procesadores(request):
    if request.method == 'GET':
        id1 = request.GET.get('procesador1')
        id2 = request.GET.get('procesador2')
        
        procesador1 = get_object_or_404(Procesador, id=id1)
        procesador2 = get_object_or_404(Procesador, id=id2)

        return render(request, 'comparacion.html', {
            'procesador1': procesador1,
            'procesador2': procesador2
        })
        
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('seleccion')  # Redirigir a la página de selección
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

from django.shortcuts import render, get_object_or_404
from .models import Procesador

def calcular_puntaje(procesador):
    puntaje = 0
    # Puedes ajustar los pesos según tu criterio
    puntaje += procesador.frecuencia_base * 10  # Peso de 10 para frecuencia base
    puntaje += procesador.numero_nucleos * 5    # Peso de 5 para núcleos
    puntaje += procesador.numero_hilos * 3       # Peso de 3 para hilos
    puntaje += (32 - procesador.tdp) * 2         # Peso de 2 para TDP (menos es mejor)
    puntaje += procesador.cache_L3 * 4            # Peso de 4 para caché L3
    return puntaje

def comparar_procesadores(request):
    if request.method == 'GET':
        id1 = request.GET.get('procesador1')
        id2 = request.GET.get('procesador2')
        
        procesador1 = get_object_or_404(Procesador, id=id1)
        procesador2 = get_object_or_404(Procesador, id=id2)

        puntaje1 = calcular_puntaje(procesador1)
        puntaje2 = calcular_puntaje(procesador2)

        mejor_procesador = procesador1 if puntaje1 > puntaje2 else procesador2

        return render(request, 'comparacion.html', {
            'procesador1': procesador1,
            'procesador2': procesador2,
            'puntaje1': puntaje1,
            'puntaje2': puntaje2,
            'mejor_procesador': mejor_procesador
        })
