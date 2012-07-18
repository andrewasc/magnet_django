# coding: utf-8

from django.shortcuts import render, HttpResponseRedirect

from .forms import ContatoSimples
from .models import Contato

def contato_simples(request):
    if request.method == 'POST': # se o form foi submetido pelo usuário
        #criamos um form associado aos dados da requisição POST
        form = ContatoSimples(request.POST)
        if form.is_valid(): # todas as validações passaram
            # Acessar dados no form cleaned_data
            contato = Contato(nome=form.cleaned_data['nome'], email=form.cleaned_data['email'])
            contato.save()
            # confirmar dados
            return render(request, 'contatos/contato_ok.html', {'form':form}) # redirecionar após POST
    else:   # o form foi submetido pelo usuário
        form = ContatoSimples() #criamos um form vazio (unbound form)

    return render(request, 'contatos/contato_simples.html', {'form': form,
    })
