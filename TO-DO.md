# 1 Create a virtual environment
python -m venv .venv
## activate the venv
venv/bin/activate
.venv/Source/activate
## Instalación Django
pip install django

## Creación apps
python manage.py startapp <Nombre App>

# Requisitos
- Create a requirements file that lists all your project's dependencies
pip freeze > requirements.txt