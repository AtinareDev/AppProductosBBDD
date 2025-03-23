# Clase para gestionar productos en el inventario
from utils.helpers import limpiar
class Producto:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def agregar_producto(self, nombre_producto, precio, cantidad, descripcion):
        """Agrega un nuevo producto al inventario"""
        query = "INSERT INTO productos (nombre_producto, precio, cantidad, descripcion) VALUES (%s, %s, %s, %s)"
        values = (nombre_producto, precio, cantidad, descripcion)
        self.db_manager.execute_query(query, values)
        limpiar()
        print("Producto agregado exitosamente.")

    def eliminar_producto(self, producto_id):
        """Elimina un producto del inventario"""
        query = "DELETE FROM productos WHERE id = %s"
        self.db_manager.execute_query(query, (producto_id,))
        limpiar()
        print("Producto eliminado exitosamente.")

    def modificar_producto(self, producto_id, nombre_producto=None, precio=None, cantidad=None, descripcion=None):
        """Modifica la información de un producto, solo cambiando los campos especificados"""
        # Empezamos con la base de la consulta
        query = "UPDATE productos SET "
        
        # Lista para almacenar las partes de la consulta (SET)
        set_clauses = []
        values = []
        
        # Agregar solo los campos que no son None
        if nombre_producto is not None:
            set_clauses.append("nombre_producto = %s")
            values.append(nombre_producto)
        if precio is not None:
            set_clauses.append("precio = %s")
            values.append(precio)
        if cantidad is not None:
            set_clauses.append("cantidad = %s")
            values.append(cantidad)
        if descripcion is not None:
            set_clauses.append("descripcion = %s")
            values.append(descripcion)
        
        # Si no se especificaron cambios, no se hace nada
        if not set_clauses:
            print("No se especificaron cambios para el producto.")
            return False

        # Unir las cláusulas SET con comas
        query += ", ".join(set_clauses)
        
        # Agregar la condición WHERE al final
        query += " WHERE id = %s"
        
        # Agregar el id del producto a los valores
        values.append(producto_id)

        # Ejecutar la consulta
        self.db_manager.execute_query(query, tuple(values))
        
        # Limpiar y mostrar mensaje de éxito
        limpiar()
        print("Producto modificado exitosamente.")
        return True


    def mostrar_productos(self):
        """Muestra todos los productos del inventario"""
        query = "SELECT * FROM productos"
        productos = self.db_manager.execute_query(query)
        if productos:
            for producto in productos:
                print(f"ID: {producto[0]}, Nombre: {producto[1]}, Precio: {producto[2]}, Cantidad: {producto[3]}, Descripción: {producto[4]}")
            return productos
        else:
            print("No hay productos en el inventario.")
