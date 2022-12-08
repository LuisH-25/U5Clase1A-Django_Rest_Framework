# Unidad 5 Clase 1A

### Instalamos 
pip install django
pip install djangorestframework

### Crear proyecto y aplicacion
django-admin startproject principal .
django-admin startapp drf

### Agregar en principal/setting
INSTALLED_APPS = [
....
    'drf',
    'rest_framework',
]

### en models de drf