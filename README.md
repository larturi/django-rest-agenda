# Agenda DRF
Api Agenda con Django Rest Framework
# Get Started:

Instalar dependencias:
```
pipenv install
```

Crear el .env
```
cp .env.dist .env

# Modificar los valores si es necesario
```

Levantar Postgres con Docker
```bash
# Levantar el entorno
docker-compose up -d

# Bajar el entorno
docker-compose down

# Borrar datos del entorno
docker-compose down -v

Crear migraciones:
```
python3 manage.py makemigrations
python3 manage.py migrate
```

Carga de datos inicial

```bash
python manage.py loaddata initial_data.json
```

Ejecutar servidor local
```
python manage.py runserver
```

##### Made with ❤️ by Leandro Arturi