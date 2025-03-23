# Aplicación de Inventario de Productos con Gestión de Usuarios

## Descripción

Esta es una aplicación de consola desarrollada en Python que permite gestionar un inventario de productos y la autenticación de usuarios a través de una base de datos MySQL. La aplicación se organiza mediante un sistema de menús en el terminal, permitiendo a los usuarios realizar acciones como registrar una cuenta, iniciar sesión, y gestionar productos en un inventario.

## Características principales:
1. **Registro de usuario**: Los usuarios pueden registrarse proporcionando un nombre de usuario único, una contraseña y un correo electrónico.
2. **Inicio de sesión**: Los usuarios pueden iniciar sesión con su nombre de usuario y contraseña para acceder a un menú donde podrán gestionar el inventario de productos.
3. **Gestión de productos**: Los usuarios autenticados pueden agregar, eliminar, modificar y visualizar productos en un inventario. Cada producto tiene un `id`, `nombre_producto`, `precio`, `cantidad` y `descripción`.

## Requisitos

- Python 3.x
- MySQL (para la base de datos)
- Las siguientes bibliotecas de Python:
  - `mysql-connector`: Para la conexión con la base de datos MySQL.
  - `os`: Para interactuar con el sistema operativo, como borrar pantallas entre menús.

## Instalación

1. **Instalar dependencias**:
   Asegúrate de tener Python 3.x instalado. Luego, instala la librería `mysql-connector` usando pip:

   ```bash
   pip install mysql-connector-python

## Base de datos

### MySql

Hay que tener una instancia de MySQL corriendo en tu máquina local o en un servidor remoto. Crea una base de datos llamada, por ejemplo, app_inventario y las siguientes tablas(sentencias sql):
``
CREATE DATABASE IF NOT EXISTS app_inventario;

USE app_inventario;

CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_usuario VARCHAR(255) NOT NULL,
    contraseña VARCHAR(255) NOT NULL,
    correo VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_producto VARCHAR(255) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    cantidad INT NOT NULL,
    descripcion TEXT
);
``
### Configuracion de la BBDD:
```
db_manager = DBManager(
    host="localhost",
    user="root",      # Cambia esto por tu usuario de MySQL
    password="",      # Cambia esto por tu contraseña de MySQL
    database="app_inventario"
)
```
### Ejecución:

Dede main.

## Estructura del código:

La aplicación se organiza en diferentes módulos para mantener un código limpio y modular:

* DB_manager.py: Maneja la conexión a la base de datos MySQL y la ejecución de las consultas SQL.
* usuarios.py: Contiene las funciones relacionadas con el registro y autenticación de usuarios.
* productos.py: Contiene las funciones relacionadas con la gestión del inventario de productos.
* menus.py: Define los menús de navegación para el registro, inicio de sesión y gestión de productos.

### Flujo:

* Menú Principal:
El usuario verá un menú con tres opciones:
    Registro: Permite crear una nueva cuenta de usuario.
    Login: Permite a un usuario autenticarse con su nombre de usuario y contraseña.
    Salir: Cierra la aplicación.

* Registro:
En el menú de registro, el usuario ingresa un nombre de usuario, una contraseña (mínimo 6 caracteres) y un correo electrónico. Si el nombre de usuario ya existe, se mostrará un error.

* Login:
El usuario debe ingresar su nombre de usuario y contraseña para acceder a un menú de gestión de productos. Si las credenciales son incorrectas, se muestra un mensaje de error.

* Menú de Productos (una vez autenticado):
    - Agregar Producto: Añadir un nuevo producto al inventario proporcionando un nombre, precio, cantidad y descripción.
    - Modificar Producto: Modificar los detalles de un producto existente.
    - Eliminar Producto: Eliminar un producto del inventario.
    - Mostrar Todos los Productos: Listar todos los productos existentes en el inventario.
    - Salir: Regresar al menú principal.

## Uso:

Registrar un usuario: Al iniciar la aplicación, elige la opción de Registro. Ingresa un nombre de usuario, una contraseña (mínimo 6     caracteres) y un correo electrónico con formato típico (ej. xxxx@xxx.com).

Iniciar sesión: Elige la opción Login y proporciona el nombre de usuario y contraseña registrados previamente. Si los datos son correctos, serás autenticado y podrás gestionar los productos.

Gestionar el inventario: Si estás autenticado, puedes elegir entre agregar, modificar, eliminar o mostrar productos en el inventario.

## Aspectos mejorables a futuro:
* Introducir encriptación en la contraseña
* Mejorar errores y comunicaciones con el usuario
* Faltan pruebas unitarias
* Revisar si la estructura de carpetas es correcta