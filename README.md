# Caso de Estudio Genérico: Creación de aplicación web con persistencia y autenticación.
## Opción de Proyecto 1: Sistema de Gestión de Inventarios
Resumen:

Implementar un sistema de gestión de inventarios para pequeñas y medianas empresas que permita el seguimiento de productos, proveedores y pedidos. Los usuarios podrán gestionar el inventario, crear pedidos de compra y venta, y generar informes de stock.

El proyecto Gestion de Inventario presenta las siguiente funcionalidades:

Formulario de registro: Los usuarios pueden crear cuentas personalizadas para gestionar sus tareas de manera segura y privada. El proceso de registro es sencillo e intuitivo.

Inicio de Sesión: Accede a tu cuenta de manera rápida y segura. La autenticación de usuarios garantiza que solo tú puedas ver y gestionar tus tareas.

Los usuarios podrán gestionar el inventario, es decir, crear pedidos de compra y venta, y generar informes de stock.

# ESTRUCTURA DEL PROYECTO
![directorio](https://github.com/DieGoArt30/GESTION-DE-INVENTARIO/assets/149025522/ddae3e79-435b-4bd9-b16b-b832c211e720)

# INICIO DE SESION
![inicio de sesion](https://github.com/DieGoArt30/GESTION-DE-INVENTARIO/assets/149025522/4f80b937-d703-4beb-92a1-08afd39fe682)

# REGISTRO
![registro](https://github.com/DieGoArt30/GESTION-DE-INVENTARIO/assets/149025522/bd01d229-2383-41b1-b6e5-6f4b8cc1939a)

# LOGIN
![login](https://github.com/DieGoArt30/GESTION-DE-INVENTARIO/assets/149025522/caad80b4-b3bf-4e61-96cc-ac650ed26acb)

# MENU DE INICIO
![menu principal](https://github.com/DieGoArt30/GESTION-DE-INVENTARIO/assets/149025522/ef300242-6df8-49ce-9fde-b5db97105601)

# PROVEEDORES
![proveedores](https://github.com/DieGoArt30/GESTION-DE-INVENTARIO/assets/149025522/e0ac7f55-1468-45f4-9f0f-ccdad65c48c0)

# PRODUCTOS
![productos](https://github.com/DieGoArt30/GESTION-DE-INVENTARIO/assets/149025522/a2826909-63ac-41b6-8a35-005a79edb74c)

# PEDIDOS
![pedidos](https://github.com/DieGoArt30/GESTION-DE-INVENTARIO/assets/149025522/170af936-d018-4309-b9bb-1bd85e75f251)


# Pasos del proyecto
## Step 1: Configuraciones del entorno de desarrollo

1. Crear carpeta del proyecto en local Gestion_Inventario, todo trabajo a partir de este punto se realiza en el directorio del proyecto.

2. Creación de archivo archivo ```README.md```

3. Inicialización de repositorio local y vinculación con repositorio remoto en GitHub
```git init
git add .
git commit -m 'Repository initialization'
git branch -M main
git remote add origin <url_repository_github>
git push -u origin main
```

4. Creación y activación de ambiente virtual de trabajo
```
 pip install virtualenv
 python -m venv Gestion_Inventario 
 .\Gestion_Inventario\Scripts\activate
````
5. Instalación de framework Django
```
   pip install django
```
6. Creación de archivo de dependencias ```requerements.txt```
```
   pip freeze > requirements.txt
```
7. Creación de archivo .gitignore y adición de archivos y directorios ignorados: directorio: venv, archivo
   ```
   .gitignore
   ```
   
8. Creación de proyecto Django inventory_management
   ```
   django-admin startproject inventory_management
   ```
   
10. cd Gestion_Inventario # Cambia al sub-directorio para trabajos de desarrollo
   ```
  python manage.py startapp inventory
   ```

# Step 2: Diseño del modelo de datos
1. Configuración de aplicación creada en el archivo inventory_management\settings.py
```
INSTALLED_APPS = [
    ...,
    'inventory',
]
```
2. Crear archivo urls.py en inventory\urls.py
- Abre el archivo creado inventory\urls.py en el editor de código.
- Importa los módulos necesarios de Django:
```
from django.urls import path
from . import views
```

° Define las URL para cada vista creada en inventori\views.py:
```
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('proveedores/', views.listar_proveedores, name='listar_proveedores'),
    path('proveedores/agregar/', views.agregar_proveedor, name='agregar_proveedor'),
    path('productos/', views.listar_productos, name='listar_productos'),
    path('productos/agregar/', views.agregar_producto, name='agregar_producto'),
    path('pedidos/', views.listar_pedidos, name='listar_pedidos'),
    path('pedidos/agregar/', views.agregar_pedido, name='agregar_pedido'),
]
```

3. Configurar las URLs en el Proyecto Principal
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inventory.urls')),
]
```

4. Abre el archivo inventory\models.py y define el modelo base con los campos requeridos (título, descripción, fecha de creación, estado):
```
from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    TIPO_PEDIDO = (
        ('compra', 'Compra'),
        ('venta', 'Venta'),
    )

    fecha = models.DateField(auto_now_add=True)
    tipo = models.CharField(max_length=10, choices=TIPO_PEDIDO)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.tipo} - {self.producto.nombre} - {self.cantidad}'
```

5. Realizar migraciones para aplicar los cambios al modelo de datos:
```
 python manage.py makemigrations
 python manage.py migrate
```

# Step 3: Implementación de funcionalidades
1. Crea las vistas y URLs en inventory\views.py y inventory\urls.py.

1.1. Crear Vistas en inventory\views.py
   - Abre el archivo base\views.py en tu editor de código.
   - Importa los módulos necesarios de Django:
     
```
from django.shortcuts import render, get_object_or_404, redirect
from .models import Proveedor, Producto, Pedido
from .forms import ProveedorForm, ProductoForm, PedidoForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
```
2. Define las funciones de vista para cada operación:

 - Registro:

```
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
```
- Login:

```
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
```

- Listar Proveedores:

```
@login_required
def listar_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'inventory/listar_proveedores.html', {'proveedores': proveedores})
```

- Agregar Proveedores:

```
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
```

- Listar Productos:

```
@login_required
def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'inventory/listar_productos.html', {'productos': productos})
```

- Agregar Productos:

```
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
```

- Listar Pedido:

```
@login_required
def listar_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'inventory/listar_pedidos.html', {'pedidos': pedidos})
```

- Agregar Pedido:

```
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
```

# Step 4: Diseño de la Interfaz de Usuario

1. Utiliza Django Templates para diseñar las plantillas HTML en la carpeta template

- Formulario Inicio.html

![inicio](https://github.com/DieGoArt30/GESTION-DE-INVENTARIO/assets/149025522/a92b0475-949c-4ce8-90e8-1d28a0d4f175)

- Formulario de Registro:

![registro](https://github.com/DieGoArt30/GESTION-DE-INVENTARIO/assets/149025522/1eab0f81-7827-4d08-a81f-5cf9149629d1)

- Formulario de Login:

![login](https://github.com/DieGoArt30/GESTION-DE-INVENTARIO/assets/149025522/00f62c1e-9bbd-4c33-a182-3f10a3abb4c7)

- Formulario Listar proveedor:

![ñListar proveedor](https://github.com/DieGoArt30/GESTION-DE-INVENTARIO/assets/149025522/fb048ca2-0064-42da-af3e-62e45babb3e2)

- Formulario Agregar proveedor:

![agregar proveedor](https://github.com/DieGoArt30/GESTION-DE-INVENTARIO/assets/149025522/f9f4f41b-f636-4ca7-a380-d6f99a15d8a8)

- Formulario Listar Producto:

![listar producto](https://github.com/DieGoArt30/GESTION-DE-INVENTARIO/assets/149025522/edd55a89-1851-4557-a2ea-fd0e8356296d)

- Formulario Agregar Producto:

![Agregar producto](https://github.com/DieGoArt30/GESTION-DE-INVENTARIO/assets/149025522/c8b987ce-4f31-4b11-b345-4c1cabc1b996)

- Formulario Listar Pedido:

![listar pedido](https://github.com/DieGoArt30/GESTION-DE-INVENTARIO/assets/149025522/84ef064c-3321-42cc-a1a4-5cd71c7944c7)

- Formulario Agregar Pedido:

![agregar pedido](https://github.com/DieGoArt30/GESTION-DE-INVENTARIO/assets/149025522/810a1190-0be8-47f4-b78a-17b79c18d846)


# Step 5: Configuración de Django Admin

1. Registra el modelo inventory en inventory/admin.py para poder administrarlo desde Django Admin:

```
from django.contrib import admin
from .models import Proveedor, Producto, Pedido

admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(Pedido)
```

2. Crear superusuario en Django.

```
python manage.py createsuperuser

#Registro de superusuario
#User: Admin
#E-mail: example@gmail.com
#Password: xxxxx
```
# Step 6: Ejecución y Pruebas

1. Ejecuta el servidor de desarrollo de Django:

```
python manage.py runserver
```

2. Accede a la aplicación desde tu navegador y realiza pruebas para asegurarte de que todas las funcionalidades funcionen correctamente.

3. Mejora y adiciona nuevas funcionalidades.
