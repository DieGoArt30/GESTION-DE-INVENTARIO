from django.shortcuts import render, get_object_or_404, redirect
from .models import Proveedor, Producto, Pedido
from .forms import ProveedorForm, ProductoForm, PedidoForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required



def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('inicio')
    else:
        form = UserCreationForm()
    return render(request, 'inventory/registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('inicio')
    else:
        form = AuthenticationForm()
    return render(request, 'inventory/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('inicio')

def inicio(request):
    return render(request, 'inventory/inicio.html')

@login_required
def listar_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'inventory/listar_proveedores.html', {'proveedores': proveedores})
@login_required
def agregar_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_proveedores')
    else:
        form = ProveedorForm()
    return render(request, 'inventory/agregar_proveedor.html', {'form': form})
@login_required
def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'inventory/listar_productos.html', {'productos': productos})
@login_required
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm()
    return render(request, 'inventory/agregar_producto.html', {'form': form})
@login_required
def listar_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'inventory/listar_pedidos.html', {'pedidos': pedidos})
@login_required
def agregar_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_pedidos')
    else:
        form = PedidoForm()
    return render(request, 'inventory/agregar_pedido.html', {'form': form})
