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

# Crea el proyecto en forma local:
## Crea un entorno virtual
```
# crea el entorno
py -m venv venv

# activa el entorno
.\venv\Scripts\activate

# instala dependencias
pip install djangorestframework

# guardo lista de dependencias
pip freeze > requirements.txt

# instala dependencias
pip install -r requirements.txt

# crea el proyecto
django-admin startproject ecommerce_rest

# abre el proyecto en tu editor favorito
```

## Crea el usuario del proyecto
```
# cambia al directorio apps
cd ecommerce_rest/apps>

# crea el usuario
django-admin startapp users

# crea el modelo
/users/models.py

# instala
pip install django-simple-history

# instala
pip install pillow
```

## Crea las migraciones de usuario
```
# cambia al directorio ecommerce_rest
cd ecommerce_rest>

# crea migraciones
python manage.py makemigrations
```

## Crea el superusuario
```
# crea superusuario
python manage.py createsuperuser
```

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