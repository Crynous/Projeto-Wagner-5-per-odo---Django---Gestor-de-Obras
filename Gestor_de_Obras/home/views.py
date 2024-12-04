

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.models import User
from obras.models import Obra



def resumo_view(request):
    # Obter os últimos 3 usuários criados/modificados
    ultimos_usuarios = User.objects.order_by('-date_joined')[:3]
    # Obter as últimas 3 obras criadas/modificadas
    ultimas_obras = Obra.objects.order_by('-data_modificacao')[:3]

    return render(request, 'home/resumo.html', {
        'ultimos_usuarios': ultimos_usuarios,
        'ultimas_obras': ultimas_obras,
    })


def home(request):
    return render(request, 'home/index.html')


def sobre_view(request):
    return render(request, 'home/sobre.html')


