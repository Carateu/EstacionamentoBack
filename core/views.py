from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Pessoa,Veiculo,MovRotativo,MovMensalista,Mensalista
from .forms import (
    PessoaForm,
    VeiculoForm,
    RotativoForm,
    MovimentoMensalistaForm,
    MensalistaForm,
)

def home(request):
    context = {'mensagem':'Estacionamento 24/7'}
    return render(request,'core/base.html',context)


def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    context = {'pessoas' : pessoas,'form' : form}
    return render(request, 'core/lista_pessoas.html',context)


def pessoa_nova(request):
    # se alguem preencheu o formulário de Pessoas um novo form com as info
    # passadas será criado
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        # se o formulário for válido, salva
        form.save()
        # depois  da validação faz-se um redirect para o template indicado
        return redirect('/core/pessoas')


def pessoa_update(request,id):
    pessoa = Pessoa.objects.get(id=id)
    # pegando as informações do form e passando a instancia de pessoa, para o update
    form = PessoaForm(request.POST or None, instance=pessoa)
    context = {'pessoa' : pessoa, 'form' : form}

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/core/pessoas')
    else:
        return render(request, 'core/update_pessoa.html', context)


def pessoa_delete(request,id):
    pessoa = Pessoa.objects.get(id=id)
    context = {'pessoa':pessoa}
    # se for um POST, deleta e redireciona para página de pessoas
    # else(GET) redireciona para o template delete_confirm
    if request.method == 'POST':
        pessoa.delete()
        return redirect('/core/pessoas')
    else:
        return render(request, 'core/delete_confirm_pessoa.html',context)


def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    form = VeiculoForm()
    context = {'veiculos' : veiculos , 'form' : form}
    return render(request,'core/lista_veiculos.html',context)


def veiculo_novo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/core/veiculos')


def veiculo_update(request,id):
    veiculo = Veiculo.objects.get(id=id)
    form = VeiculoForm(request.POST or None, instance=veiculo)
    context = {'veiculo' : veiculo,'form' : form}

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/core/veiculos')
    else:
        return render(request, 'core/update_veiculo.html', context)


def veiculo_delete(request,id):
    veiculo = Veiculo.objects.get(id=id)
    context = {'veiculo':veiculo}
    if request.method == 'POST':
        veiculo.delete()
        return redirect('/core/veiculos')
    else:
        return render(request, 'core/delete_confirm_veiculo.html',context)



def lista_movrotativos(request):
    movrotativos = MovRotativo.objects.all()
    form = RotativoForm()
    context = {'movrotativos' : movrotativos, 'form' : form}
    return render(request,'core/lista_movrotativos.html', context)


def novo_rotativo(request):
    form = RotativoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/core/movimentosRotativos')


def rotativo_update(request,id):
    movrotativo = MovRotativo.objects.get(id=id)
    form = RotativoForm(request.POST or None, instance=movrotativo)
    context = {'movrotativo' : movrotativo,'form' : form}

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            redirect('/core/movimentosRotativos')
    else:
        return render(request, 'core/update_rotativo.html', context)


def rotativo_delete(request,id):
    movrotativo = MovRotativo.objects.get(id=id)
    context = {'movrotativo':movrotativo}
    if request.method == 'POST':
        movrotativo.delete()
        return redirect('/core/movimentosRotativos')
    else:
        return render(request, 'core/delete_confirm_rotativo.html',context)



def lista_movMensal(request):
    form = MovimentoMensalistaForm()
    movmensais = MovMensalista.objects.all()
    context = {'movmensais' : movmensais, 'form' : form}
    return render(request,'core/lista_movMensal.html',context)


def movMensal_novo(request):
    form = MovimentoMensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/core/movimentosMensais')


def movMensal_update(request,id):
    movmensal = MovMensalista.objects.get(id=id)
    form = MovimentoMensalistaForm(request.POST or None, instance=movmensal)
    context = {'movmensal' : movmensal, 'form' : form} 

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            redirect('/core/movimentosMensais')
    else:
        return render(request, 'core/update_movmensal.html', context)


def movMensal_delete(request,id):
    movMensal = MovMensalista.objects.get(id=id)
    context = {'movMensal':movMensal}
    if request.method == 'POST':
        movMensal.delete()
        return redirect('/core/movimentosMensais')
    else:
        return render(request, 'core/delete_confirm_movMensais.html', context)



def lista_mensalistas(request):
    form = MensalistaForm()
    mensalistas = Mensalista.objects.all()
    context = {'mensalistas' : mensalistas, 'form' : form}
    return render(request,'core/lista_mensalistas.html',context)


def mensalista_novo(request):
    form = MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/core/mensalistas')


def mensalista_update(request,id):
    mensalista = Mensalista.objects.get(id=id)
    form = MensalistaForm(request.POST or None, instance=mensalista)
    context = {'mensalista' : mensalista, 'form' : form}

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            redirect('/core/mensalistas')
    else:
        return render(request, 'core/update_mensalista.html', context)
        

def mensalista_delete(request,id):
    mensalista = Mensalista.objects.get(id=id)
    context = {'mensalista':mensalista}
    if request.method == 'POST':
        mensalista.delete()
        return redirect('/core/mensalistas')
    else:
        return render(request, 'core/delete_confirm_mensalista.html', context)
