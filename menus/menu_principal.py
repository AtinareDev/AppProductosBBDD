from utils.helpers import limpiar


def menu_principal():
    while True:
        print("Bienvenido al sistema de gestión de productos Christian 1.0")
        print("1. Login de usuario")
        print("2. Registro de usuario")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            print("Registro de usuario")
            limpiar()

        elif opcion == "2":
            print("Login de usuario")
            limpiar()

            
        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
