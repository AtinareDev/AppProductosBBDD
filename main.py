# Configuración de la conexión y ejecución
from conexion.DB_manager import DBManager
from menus.menus import Menu


def main():
    db_manager = DBManager('localhost', 'root', '', 'inventario_app')
    db_manager.connect()

    # Crear las tablas si no existen
    db_manager.execute_query("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre_usuario VARCHAR(255) NOT NULL,
            contraseña VARCHAR(255) NOT NULL,
            correo VARCHAR(255) NOT NULL UNIQUE
        );
    """)

    db_manager.execute_query("""
        CREATE TABLE IF NOT EXISTS productos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre_producto VARCHAR(255) NOT NULL,
            precio DECIMAL(10, 2) NOT NULL,
            cantidad INT NOT NULL,
            descripcion TEXT
        );
    """)

    menu = Menu()
    menu.set_db_manager(db_manager)
    menu.mostrar_menu_principal()
    db_manager.close()


if __name__ == "__main__":
    main()
