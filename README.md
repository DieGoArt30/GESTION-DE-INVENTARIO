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

