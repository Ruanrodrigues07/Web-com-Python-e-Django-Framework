from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from django.template import loader

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

    context = {
        'nome': 'Ruan Rodrigues',
        'email': 'ruan.arjoaquim@outlook.com',
        'linkedin': 'ruanrodrigues07',
        'github': 'ruanrodrigues07',
        'cabecalho': 'programação web com django framework',
    }

    return render(request, 'contato.html', context)

def produto(request, pk):
    # produto = Produto.objects.get(id=pk)
    produto = get_object_or_404(Produto, id=pk)

    context = {
        'produto': produto,
        'cabecalho': 'programação web com django framework',
    }
    return render(request, 'produto.html', context)

def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf-8', status=404)


def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf-8', status=500)