from django.shortcuts import render

def index(request):
    context = {
        'curso': 'programação web com django framework',
        'outro': 'curso de python',
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')