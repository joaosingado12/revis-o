from django.shortcuts import render, redirect
from .models import Jogadores

# Create your views here.

def home(request):
    jogadores = Jogadores.objects.all()
    return render(request, 'home.html', {'jogadores': jogadores})

def salvar(request):
    vnome = request.POST.get('nome')
    vnumero= request.POST.get('numero')
    vidade= request.POST.get('idade')
    valtura= request.POST.get('altura')
    vtime= request.POST.get('time')
    vposicao= request.POST.get('posicao')
    Jogadores.objects.create(nome=vnome, numero=vnumero, idade=vidade, altura=valtura, time=vtime, posicao=vposicao)
    return redirect(home)
    

def editar(request, id):
    jogador = Jogadores.objects.get(id=id)
    return render(request, "editar.html", {'jogador': jogador})

def update(request, id):
    jogador = Jogadores.objects.get(id=id)
    
    nome = request.POST.get("nome")
    numero = request.POST.get("numero")
    idade = request.POST.get("idade")
    altura = request.POST.get("altura")
    time = request.POST.get("time")
    posicao = request.POST.get("posicao")

    jogador.nome = nome
    jogador.numero = numero
    jogador.idade = idade
    jogador.altura = altura
    jogador.time = time
    jogador.posicao = posicao
        
    jogador.save()
    return redirect(home)

def excluir(request, id):
    jogador = Jogadores.objects.get(id=id)
    jogador.delete()
    return redirect(home)