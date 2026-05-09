# Proyecto Final de Python - Coderhouse

Hola. Este es el repositorio de mi proyecto final para el curso de Python dictado en Coderhouse. Se trata de una aplicación web desarrollada con Django que funciona como un blog interactivo, integrando un sistema completo de usuarios, perfiles, mensajería y operaciones CRUD.

Desarrollado por Juan Cruz Escobar.

## Funcionalidades principales

El proyecto fue diseñado cumpliendo con todos los requisitos de la rúbrica de evaluación:

- Sección de Blog (/pages/): Un espacio donde se listan los artículos creados. Permite ver el detalle de cada post, además de crear, editar y eliminar artículos (CRUD). El editor de texto integra CKEditor para soportar formato enriquecido y carga de imágenes.
- Gestión de Usuarios (/accounts/): Incluye registro, inicio y cierre de sesión. Cada usuario cuenta con un perfil propio donde puede actualizar su biografía, subir una foto de avatar y cambiar su contraseña de forma segura.
- Mensajería (/mensajes/): Una bandeja de entrada donde los usuarios logueados pueden ver los mensajes recibidos por parte de otros usuarios.
- Acerca de mí (/about/): Una vista estática a modo de presentación personal y profesional.
- Panel de Administración (/admin/): Todos los modelos de la base de datos (Artículos, Mensajes, Cursos, Estudiantes, etc.) están registrados y pueden ser administrados por un superusuario.

## Tecnologías utilizadas

- Backend: Python 3 y Django.
- Base de Datos: SQLite3.
- Frontend: HTML5, CSS3, Bootstrap 5 y el sistema de templates de Django.
- Librerías adicionales: django-ckeditor.

## Video de presentación

En el siguiente enlace se puede ver un recorrido completo por la plataforma web, demostrando el funcionamiento de todas las vistas y herramientas requeridas en la entrega final:

https://drive.google.com/drive/folders/10X9wjLgccZ5BKcWWxYEfuVc7d79LseI2?usp=sharing

Gracias por revisar el proyecto.