from django.shortcuts import render, redirect
from .models import Jogadores, Clube

# Create your views here.

def home(request):
    jogadores = Jogadores.objects.all()
    clubes = Clube.objects.all()
    return render(request, 'home.html', {'jogadores': jogadores, 'clubes': clubes})

def novo(request):
     clubes = Clube.objects.all()
     return render(request, 'novo.html', {'clubes': clubes})

def salvar(request):
    vnome = request.POST.get('nome')
    vnumero= request.POST.get('numero')
    vidade= request.POST.get('idade')
    valtura= request.POST.get('altura')

    clube_id = request.POST.get("clube")
    vclube= Clube.objects.get(id=clube_id) 

    vposicao= request.POST.get('posicao')
    vdescricao = request.POST.get('posicao')
    Jogadores.objects.create(nome=vnome, numero=vnumero, idade=vidade, altura=valtura, clube=vclube, posicao=vposicao, descricao=vdescricao)
    
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

    clube_id = request.POST.get("clube")
    clube = Clube.objects.get(id=clube_id)

    posicao = request.POST.get("posicao")
    descricao = request.POST.get("descricao")

    jogador.nome = nome
    jogador.numero = numero
    jogador.idade = idade
    jogador.altura = altura
    jogador.clube = clube
    jogador.posicao = posicao
    jogador.descricao = descricao
        
    jogador.save()
    return redirect(home)

def excluir(request, id):
    jogador = Jogadores.objects.get(id=id)
    jogador.delete()
    return redirect(home)

def clube(request, id):
    clube = Clube.objects.get(id=id)
    clubes = Clube.objects.all()
    jogadores = Jogadores.objects.filter(clube=clube)
    return render(request, 'clube.html', {'jogadores': jogadores, 'clube': clube, 'clubes': clubes})