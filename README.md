# bd_biblioteca3

# Sistema de gestión de biblioteca

## Descripción

Este proyecto consiste en una aplicación CRUD desarrollada en Python que se conecta a una base de datos MySQL para gestionar la información de una biblioteca.

El sistema permite crear, consultar, actualizar y eliminar registros relacionados con socios, bibliotecarios, autores, editoriales, géneros literarios, libros, ejemplares físicos y préstamos.

## Funcionalidades

- **Socios:** registrar, consultar, modificar y eliminar socios.
- **Bibliotecarios:** administrar los datos del personal responsable.
- **Autores:** registrar y administrar autores.
- **Editoriales:** registrar y administrar editoriales.
- **Géneros:** administrar los géneros literarios.
- **Libros:** registrar libros y consultar sus datos junto con su editorial y género.
- **Ejemplares:** administrar los ejemplares físicos, su estado y ubicación.
- **Relación libro-autor:** asociar autores con los libros correspondientes.
- **Préstamos:** registrar, consultar, modificar y eliminar préstamos. Al registrar un préstamo, el ejemplar cambia a estado `Prestado`; al eliminarlo, vuelve a `Disponible`.

## Tecnologías utilizadas

- Python
- MySQL
- MySQL Connector/Python
- python-dotenv
- Clever Cloud (alojamiento de la base de datos)
- Git y GitHub

## Requisitos

- Python 3 instalado.
- Una base de datos MySQL creada y alojada en Clever Cloud.
- Las credenciales de conexión correspondientes.

## Seguridad

- El archivo `.gitignore` evita que `.env` se incluya en los cambios de Git.
- Las credenciales reales se entregan por separado en el documento de texto solicitado en Classroom.

## Archivos principales

- `crud.py`: código Python con las operaciones CRUD.
- `.gitignore`: archivos y carpetas que Git debe ignorar.
- `requirements.txt`: dependencias necesarias para ejecutar el programa.
