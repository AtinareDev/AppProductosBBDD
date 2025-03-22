import re
from utils.helpers import limpiar


def registrar_usuario():
    print("=== Registro de Usuario ===")

    # Validación del nombre (solo letras y mínimo 3 caracteres)
    while True:
        nombre = input(
            'Ingrese su nombre (escriba "SALIR" para cancelar): ').strip()
        if nombre.lower() == "salir":
            print("🚪 Registro cancelado.")
            return None  # Salimos de la función sin devolver datos
        if re.match(r"^[A-Za-záéíóúüñÁÉÍÓÚÜÑ\s]{3,}$", nombre):
            break
        print("❌ Nombre inválido. Debe contener solo letras y al menos 3 caracteres.")

    # Validación del correo (formato correcto con @ y dominio)
    while True:
        correo = input("Ingrese su correo electrónico: ").strip()
        if correo.lower() == "salir":
            print("🚪 Registro cancelado.")
            return None
        if re.match(r"^[\w\.-]+@[\w\.-]+\.\w{2,4}$", correo):
            break
        print("❌ Correo inválido. Asegúrate de ingresar un correo válido (ej: usuario@email.com).")

    # Validación de contraseña (mínimo 6 caracteres y al menos un número)
    while True:
        contraseña = input(
            "Ingrese su contraseña (mínimo 6 caracteres, al menos un número): ").strip()
        if contraseña.lower() == "salir":
            print("🚪 Registro cancelado.")
            return None
        if len(contraseña) >= 6 and re.search(r"\d", contraseña):
            break
        print("❌ Contraseña insegura. Debe tener al menos 6 caracteres y contener al menos un número.")

    # Simulación de almacenamiento del usuario
    limpiar()
    print(f"✅ Usuario '{nombre}' con correo {correo} registrado con éxito.")
    return nombre, correo, contraseña
