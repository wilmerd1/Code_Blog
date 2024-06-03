## Proyecto CoderHouse

Comisión: 54135
Alumno: Wilmer Andres Duque Olaya


## Acerca del proyecto

Se creo una aplcación de blog, donde permita crear un post y agregar una imagen.
Contienelos archivos estaticos (html, css, js) y principales de la aplicación, donde el template base en encarga de enviar la plantilla principal del NavBar y footer para todas las demás aplicaciones.

1. Home: se cargan los 3 ultimos y 2 primero post de acuerdo con la fecha de creación
2. Post: permite cargar todos los posts creados, mostrando la imagen que se cargo, titulo, subtitulo, imagen del usuario que creo el post, nombre y fecha de creación.
3. Add Post: Muestra forms que permite crear un post se uso la libreria de Summernote que ayuda al usuario funcional la creación de los comentarios.
4. About: Información desarrollador
5. Login: 
6. Sign Up: 
7. User

## Aplicaciones


## Modelos

Se tiene el modelo de Post y otro para el manejo del Avatar.

## Mejoras Futuras

1. Mejorar la interfaz visual, en la pagina principal
2. Mejor redireccionamiento de la pagina

## Problemas conocidos

3. Validaciones y restricciones a nivel de forms y base de datos
4. Direcciones URL en la navegación

# Code_Blog

To run the Code_Blog application locally, please follow these steps:

1. Clone the repository to your local machine using the following command:

   ```
   git clone https://github.com/wilmerd1/Code_Blog.git
   ```

2. Navigate to the project directory:

   ````
   cd Code_Blog
   ```

3. Create a virtual environment and activate it (optional but recommended):

   ````
   python -m venv venv
   source venv/bin/activate
   ```

4. Install the project dependencies:

   ````
   pip install -r requirements.txt
   ```

5. Apply the database migrations:

   ````
   python manage.py migrate
   ```

6. Create a superuser (admin) account:

   ````
   python manage.py createsuperuser
   ```

   Follow the prompts to enter your desired username and password.

7. Start the development server:

   ````
   python manage.py runserver
   ```

8. Open your web browser and access the application at [http://localhost:8000](http://localhost:8000).

9. To access the admin dashboard, go to [http://localhost:8000/admin](http://localhost:8000/admin) and login with your superuser account.
