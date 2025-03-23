# Clase para gestionar la navegación de los menús
from conexion.usuarios import Usuario
from productos import Producto
from utils.helpers import limpiar
from mysql.connector import Error

class Menu:
    def __init__(self):
        self.db_manager = None
        self.usuario = None
        self.producto = None

    def set_db_manager(self, db_manager):
        """Configura el gestor de la base de datos"""
        self.db_manager = db_manager
        self.usuario = Usuario(db_manager)
        self.producto = Producto(db_manager)

    def mostrar_menu_principal(self):
        """Muestra el menú principal y navega entre opciones"""
        while True:
            print("\nMenú Principal:")
            print("1. Login")
            print("2. Registro")
            print("3. Salir")
            opcion = input("Seleccione una opción: ")
            if opcion == '1':
                self.mostrar_menu_login()
            elif opcion == '2':
                self.mostrar_menu_registro()
            elif opcion == '3':
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida.")

    def mostrar_menu_registro(self):
        """Muestra el menú de registro"""
        nombre_usuario = input("Ingrese nombre de usuario: ")
        contraseña = input("Ingrese contraseña: ")
        correo = input("Ingrese correo: ")
        self.usuario.registrar_usuario(nombre_usuario, contraseña, correo)

    def mostrar_menu_login(self):
        """Muestra el menú de login"""
        nombre_usuario = input("Ingrese nombre de usuario: ")
        contraseña = input("Ingrese contraseña: ")
        if self.usuario.autenticar_usuario(nombre_usuario, contraseña):
            limpiar()
            print("¡Login exitoso!")
            self.mostrar_menu_inventario()
        else:
            print("Nombre de usuario o contraseña incorrectos.")


    def mostrar_menu_inventario(self):
        """Muestra el menú de inventario (después de login exitoso)"""
        while True:
            print("\nMenú Inventario:")
            print("1. Agregar Producto")
            print("2. Eliminar Producto")
            print("3. Modificar Producto")
            print("4. Mostrar Productos")
            print("5. Salir")
            opcion = input("Seleccione una opción: ")
            if opcion == '1':
                limpiar()
                nombre_producto = input("Nombre del producto: ")
                precio = float(input("Precio del producto: "))
                cantidad = int(input("Cantidad del producto: "))
                descripcion = input("Descripción del producto: ")
                self.producto.agregar_producto(nombre_producto, precio, cantidad, descripcion)
            elif opcion == '2':
                limpiar()
                producto_id = int(input("ID del producto a eliminar: "))
                self.producto.eliminar_producto(producto_id)
            elif opcion == '3':
                limpiar()
               
                # Obtener los productos existentes
                productos = self.producto.mostrar_productos()
                if productos:
                    # Extraer los IDs de los productos existentes
                    producto_ids = [producto[0] for producto in productos]

                    # Control de entrada para el ID del producto
                    while True:
                        try:
                            producto_id = int(input("ID del producto a modificar: "))
                            # Verificar si el producto ID existe en los productos
                            if producto_id not in producto_ids:
                                print("Error: El ID ingresado no existe en el inventario. Inténtalo de nuevo.")
                            else:
                                break
                        except ValueError:
                            print("Error: El ID debe ser un número entero. Inténtalo de nuevo.")

                    # Control de entrada para el nombre del producto
                    nuevo_nombre = input("Nuevo nombre del producto: ")
                    # Si el nombre está vacío, lo dejamos igual que antes
                    if nuevo_nombre == "":
                        nuevo_nombre = None   

                    # Control de entrada para el precio
                    while True:
                        try:
                            nuevo_precio_str = input("Nuevo precio del producto: ")
                            if nuevo_precio_str == "":  # Si está vacío, mantenemos el valor anterior
                                nuevo_precio = None  
                                break
                            else:
                                nuevo_precio = float(nuevo_precio_str)  # Intentamos convertir a float
                                break
                        except ValueError:
                            print("Error: El precio debe ser un número válido. Se establecerá como 0.")

                    # Control de entrada para la cantidad
                    while True:
                        try:
                            nueva_cantidad_str = input("Nueva cantidad del producto: ")
                            if nueva_cantidad_str == "":  # Si está vacío, mantenemos el valor anterior
                                nueva_cantidad = None
                                break
                            else:
                                nueva_cantidad = int(nueva_cantidad_str)  # Intentamos convertir a entero
                                break
                        except ValueError:
                            print("Error: La cantidad debe ser un número válido. Se establecerá como 0.")

                    # Control de entrada para la descripción
                    nueva_descripcion = input("Nueva descripción del producto: ")
                    if nueva_descripcion == "":
                        nueva_descripcion = None

                    # Ahora pasamos los valores a la función para modificar el producto
                    self.producto.modificar_producto(producto_id, nuevo_nombre, nuevo_precio, nueva_cantidad, nueva_descripcion)


            elif opcion == '4':
                limpiar()
                self.producto.mostrar_productos()
            elif opcion == '4':
                limpiar()
                self.producto.mostrar_productos()
            elif opcion == '5':
                limpiar()
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida.")