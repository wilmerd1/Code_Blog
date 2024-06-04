# 1 Create a virtual environment
python -m venv .venv
## activate the venv
venv/bin/activate
.venv/Source/activate

## Instalación requirements
-- pip freeze > requirements.txt
pip install -r requirements.txt

## Creación apps
django-admin startproject config .
python manage.py startapp <Nombre App>


## Create a superuser (admin) account:
python manage.py createsuperuser
admin
123

