# Unidad 5 Clase 1A

### Instalamos 
* pip install django
* pip install djangorestframework

### Crear proyecto y aplicacion
* django-admin startproject principal .
* django-admin startapp drf

### Agregar en principal/setting
INSTALLED_APPS = [
....
    'drf',
    'rest_framework',
]

### archivos nuevos y editados
* drf/serializaers.py
* drf/urls.py
* drf/views.py

### ingresar en REST framework
{
  "nombre": "Peru",
  "moneda":"sol"
}
### PAra mayor informacion
https://www.django-rest-framework.org/topics/documenting-your-api/

### Link de la clase
https://www.youtube.com/watch?v=3-mKdyApnz4
