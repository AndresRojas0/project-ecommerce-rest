# project-ecommerce-rest
Es una práctica de Django Rest Framework
[Curso Django Rest Framework](https://www.youtube.com/playlist?list=PLMbRqrU_kvbRI4PgSzgbh8XPEwC1RNj8F)

# Descripción del Proyecto
project-ecommerce-rest es un ejemplo de lógica de aplicación web tipo _ecommerce_ con tecnología REST API.

# Instrucciones de Uso
Clona este repositorio en tu host.

# Consoles -> bash
* git clone https://github.com/AndresRojas0/project-ecommerce-rest
* Navega hasta el directorio del proyecto.
* cd mi-pagina-de-inicio  
* Ejecuta el archivo manage.py

## Consoles -> bash: crea el proyecto de cero
* ``` py -m venv venv ``` crea el entorno
* ``` .\venv\Scripts\activate ``` activa el entorno
* ``` pip install djangorestframework ``` instala dependencias
* ``` pip freeze > requirements.txt ``` guardo lista de dependencias
* ``` pip install -r requirements.txt ``` instala dependencias
* ``` django-admin startproject ecommerce_rest ``` crea el proyecto
* abre el proyecto en tu editor favorito

## Consoles -> bash: crea el usuario del proyecto
* ``` cd ecommerce_rest/apps> ``` cambia al directorio apps
* ``` django-admin startapp users ``` crea el usuario
* ``` /users/models.py ``` crea el modelo
* ``` pip install django-simple-history ``` instala
* ``` pip install pillow ``` instala

## Consoles -> bash: crea las migraciones de usuario
* ``` cd ecommerce_rest> ``` cambia al directorio ecommerce_rest
* ``` python manage.py makemigrations ``` crea migraciones

## Consoles -> bash: crea el superusuario
* ``` python manage.py createsuperuser ``` crea superusuario

# Despliegue
El proyecto no se encuentra desplegado (19/01/2025).

# Funcionalidades
* Acceder a los endpoints API.

# Tecnologías Utilizadas
[![Languages](https://skillicons.dev/icons?i=python,django)](https://skillicons.dev)

# Autores
Este proyecto fue desarrollado como práctica por Andrés Rojas.

# Licencia
Este proyecto está bajo la licencia MIT.