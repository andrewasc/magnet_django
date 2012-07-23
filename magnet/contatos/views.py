# coding: utf-8

from django.shortcuts import render, HttpResponseRedirect
from django.forms.formsets import formset_factory
from django.forms.models import inlineformset_factory

from .forms import ContatoSimples, FoneForm, ContatoModelForm, FoneModelForm
from .models import Contato, Fone

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

def contato_fones(request):
    FonesFormSet = formset_factory(FoneForm)
    if request.method == 'POST': # se o form foi submetido pelo usuário
        #criamos um form associado aos dados da requisição POST
        form_contato = ContatoSimples(request.POST)
        forms_fones = FonesFormSet(request.POST)
        if form_contato.is_valid() and forms_fones.is_valid(): # todas as validações passaram
            # Acessar dados no form cleaned_data
            contato = Contato(nome=form_contato.cleaned_data['nome'], email=form_contato.cleaned_data['email'])
            contato.save()
            for form_fone in forms_fones:
                fone = Fone(contato=contato,
                            tipo=form_fone.cleaned_data['tipo'],
                            ddd=form_fone.cleaned_data['ddd'],
                            numero=form_fone.cleaned_data['numero'],)
                fone.save()
            # confirmar dados
            return render(request, 'contatos/contato_ok.html', {'form_contato': form_contato,  'forms_fones': forms_fones}) # redirecionar após POST
    else:   # o form foi submetido pelo usuário
        form_contato = ContatoSimples() #criamos um form vazio (unbound form)
        forms_fones = FonesFormSet()
    return render(request, 'contatos/contato_fones.html', {'form_contato': form_contato, 'forms_fones': forms_fones
    })



def contato_simples_com_modelform(request):
    if request.method == 'POST': # se o form foi submetido pelo usuário
        #criamos um form associado aos dados da requisição POST
        form = ContatoModelForm(request.POST)
        if form.is_valid(): # todas as validações passaram
            #salvar instância do modelo associado ao form
            form.save()
            # confirmar dados
            return render(request, 'contatos/contato_ok.html', {'form':form}) # redirecionar após POST
    else:   # o form foi submetido pelo usuário
        form = ContatoSimples() #criamos um form vazio (unbound form)

    return render(request, 'contatos/contato_simples.html', {'form': form,
    })



def contato_fones_com_modelform(request):
    FonesFormSet = inlineformset_factory(Contato, Fone)
    if request.method == 'POST': # se o form foi submetido pelo usuário
        #criamos um form associado aos dados da requisição POST
        form_contato = ContatoModelForm(request.POST)
        if form_contato.is_valid(): # todas as validações passaram
            form_contato.save()
            forms_fones = FonesFormSet(request.POST, intance=contato)
            forms_fones.save()
            # confirmar dados
            return render(request, 'contatos/contato_ok.html', {'form_contato': form_contato,  'forms_fones': forms_fones}) # redirecionar após POST
        else:
            forms_fones = FonesFormSet(request.POST)
    else:   # o form foi submetido pelo usuário
        form_contato = ContatoModelForm() #criamos um form vazio (unbound form)
        forms_fones = FonesFormSet()
    return render(request, 'contatos/contato_fones.html', {'form_contato': form_contato, 'forms_fones': forms_fones
    })

