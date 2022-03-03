# pausas_activas
Proyecto de Pausas Activas en HTML/CSS/JS y Django


# Introduction

Pausas activas busca administrar una lista de ejercicios que propone mejorar la calidad de vida y salud en el trabajo. 

### Main features

* Responsivo y personalizable

* Materialize static files incluídos

* CRUD de Sistema, tipo de pausa y actividades

* SQLite está por defecto si no especifica entorno virtual

# Corre!

Para usar este sistema en tu propio proyecto

### Entorno virtual existente:

Si tu proyecto tiene un entorno virtual predefinido, primero configura Python (preferiblemente en versión 3.9)

Y luego corre el comando pip install -r requierements.txt

Para iniciar sesión en el sitio de administración, necesitamos una cuenta de usuario con estado de Personal habilitado. Para ver y crear registros tambien necesitamos que este usuario tenga permisos para administrar todos nuestros objetos. Puedes crear una cuenta  "administrador" que tenga acceso total al sitio y a todos los permisios necesarios usando manage.py:

$ python manage.py createsuperuser

IMPORTANTE: Diligencia la administración de contenidos sugiriendo una contraseña segura.

Para iniciar sesión en el sitio, ve a la URL /admin (e.j. http://127.0.0.1:8000/admin) e ingresa tus credenciales de id usuario y contraseña de administrador (serás redirigido a la página login, y entonces volverás a la URL de /admin después de haber ingresado tus datos)

Después de instalar las dependencias, ejecuta el servidor 

$ python manage.py runserver

### Despliegue Docker:

$ docker -compose --build
$ docker -compose --up



