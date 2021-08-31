import cliente
from django.shortcuts import redirect, render
from .models import Cliente
from .form import ClienteForm
from django.core.paginator import Paginator


def index(request):
    # list_clientes = Cliente.objects.all()
    list_clientes = Cliente.objects.order_by('data_criacao').filter(
        categoria=2
    )
    paginator = Paginator(list_clientes, 10)
    page = request.GET.get('page')
    list_clientes = paginator.get_page(page)
    return render(request, 'cliente/index.html', {'clientes': list_clientes})


def detail(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    return render(request, 'cliente/detalhe.html', {'cliente': cliente})


def create(request):
    form = ClienteForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('cliente')


def form(request):
    data = {}
    data['form'] = ClienteForm()
    return render(request, 'cliente/form.html', data)


def edit(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    form = ClienteForm(instance=cliente)
    return render(request, 'cliente/form.html', {'cliente': cliente, 'form': form})


def update(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    form = ClienteForm(request.POST, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect('cliente')


def delete(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    cliente.delete()
    return redirect('cliente')
