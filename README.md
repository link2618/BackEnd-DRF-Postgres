<h1>Proyecto de prueba con Django Rest Framework</h1>

En este proyecto se utiliza Django Rest Framework (DRF) para crear la parte logica de un proyecto. La BD utilizada es PostgreSQL.

<details>
  <summary>Ver enlaces de Swagger</summary>
  
  [Swagger2](https://mvnrepository.com/artifact/io.springfox/springfox-swagger2) <br>
  [Swagger UI](https://mvnrepository.com/artifact/io.springfox/springfox-swagger-ui)
</details>

##Pasos para librerias instaladas

- Django Rest Framework <br>
`pip install djangorestframework`

- Postgres <br>
`pip install psycopg2`

- Para variables de entorno<br>
``pip install python-decouple``

##Migracion para la BD

-Primera vez: para crear tablas por default<br>
`python manage.py migrate`

-Para realizar cambios de los modelos<br>
`python manage.py makemigrations`<br>
`python manage.py migrate`

-Obtener SQL de migracion<br>
`python manage.py sqlmigrate api 0001_initial`

##Creacion de APPS

`python manage.py startapp {{NombreApp}}`

#Crear requeriment
`pip freeze > requirements.txt`<br>
Para instalarlos<br>
`pip install -r requirements.txt`