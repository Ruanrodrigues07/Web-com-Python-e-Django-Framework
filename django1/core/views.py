from django.shortcuts import render

def index(request):
    print(dir(request))
    print(f'User: {request.user}')
    if str(request.user) == "AnonymousUser":
        teste = "Usuário anônimo"
    else:
        teste = "Usuário logado"
    context = {
        'curso': 'programação web com django framework',
        'outro': 'curso de python',
        'logado': teste,
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')