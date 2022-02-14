from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from contas.models import Cliente, Filme, Locacao

def index(request):
# Contando o número de livros e exemplares:
    num_cliente = Cliente.objects.all().count()
    num_filme = Filme.objects.all().count()
    num_locacao = Locacao.objects.all().count()

    contexto = {
        'num_cliente': num_cliente,
        'num_filme': num_filme,
        'num_locacao': num_locacao,
    }
    # Renderizando o template index.html com os dados da variável contexto:
    return render(request, 'index.html', context=contexto)


class ClienteListView(generic.ListView):
    model = Cliente

class ClienteDetailView(generic.DetailView):
    model = Cliente

class ClienteCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'contas.pode_manipular'
    model = Cliente
    fields = '__all__'

class ClienteUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'contas.pode_manipular'
    model = Cliente
    fields = ['nome', 'cpf', 'data_nascimento']

class ClienteDelete(PermissionRequiredMixin, DeleteView):
        permission_required = 'contas.pode_manipular'
        model = Cliente

        def get_success_url(self):
            return reverse('cliente')

#Filme

class FilmeListView(generic.ListView):
    model = Filme

class FilmeDetailView(generic.DetailView):
    model = Filme

class FilmeCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'contas.pode_manipular'
    model = Filme
    fields = '__all__'

class FilmeUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'contas.pode_manipular'
    model = Filme
    fields = ['titulo', 'genero', 'produtora']

class FilmeDelete(PermissionRequiredMixin, DeleteView):
        permission_required = 'contas.pode_manipular'
        model = Filme

        def get_success_url(self):
            return reverse('filme')
#Locacao

class LocacaoListView(generic.ListView):
    model = Locacao

class LocacaoDetailView(generic.DetailView):
    model = Locacao

class LocacaoCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'contas.pode_manipular'
    model = Locacao
    fields = '__all__'

class LocacaoUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'contas.pode_manipular'
    model = Locacao
    fields = ['cliente', 'filme', 'valor']

class LocacaoDelete(PermissionRequiredMixin, DeleteView):
        permission_required = 'contas.pode_manipular'
        model = Locacao

        def get_success_url(self):
            return reverse('locacao')