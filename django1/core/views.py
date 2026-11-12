from django.shortcuts import render

from core.models import Produto

def index(request):
    produtos = Produto.objects.all()

    context = {
        'curso': 'programação web com django framework',
        'outro': 'curso de python',
        'produtos': produtos,
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')

def produto(request, pk):
    produto = Produto.objects.get(id=pk)

    context = {
        'produto': produto
    }
    return render(request, 'produto.html', context)