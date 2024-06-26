# Caso de Estudio Genérico: Creación de aplicación web con persistencia y autenticación.
## Opción de Proyecto 1: Sistema de Gestión de Inventarios
Resumen:

Implementar un sistema de gestión de inventarios para pequeñas y medianas empresas que permita el seguimiento de productos, proveedores y pedidos. Los usuarios podrán gestionar el inventario, crear pedidos de compra y venta, y generar informes de stock.

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

9. cd Gestion_Inventario # Cambia al sub-directorio para trabajos de desarrollo  
```
  python manage.py startapp inventory
```

