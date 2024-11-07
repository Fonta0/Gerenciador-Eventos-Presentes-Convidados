from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    if request.method == "GET":
        return render(request, 'home.html')
    elif request.method == "POST":
        nome_presente = request.POST.get('nome_presente')
        preco = request.POST.get('preco')
        importancia = request.get('importancia')
        foto = request.Files.get('foto')

        return HttpResponse("Teste")

    

