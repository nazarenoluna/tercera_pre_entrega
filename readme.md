# ProyectoCoder

## Pagina web en Django
+ Consta con 3 modelos (Profesores, Cursos y Estudiantes)
+ Tiene formularios para agregar en los 3 modelos en la base de datos y uno adicional de buscar por nombre  en Cursos


## Instrucciones instalar proyecto en local
+ Crea una carpeta contenedora madre
+ Abre la consola y ubicate en la carpeta madre
+ Crea y activa el ambiente virtual
+ Clona el proyecto
+ Entra en la carpeta que acabas de clonar
+ Para instalar las dependencias corre este comando:

```
pip install -r requirements.txt
```

## Instrucciones para entrar al panel aministrativo de Django

+ Acceder con user y password via:
```
127.0.0.1:8000/admin
```
+ Usuario superuser creado (en la base de datos)

+ Usuario = admin
+ Password = 1234abcd

+ Sino en consola, crear un superuser:
```
python manage.py createsuperuser
```