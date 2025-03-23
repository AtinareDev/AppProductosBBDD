# Clase para gestionar usuarios (registro y autenticación)
import re
from utils.helpers import limpiar

class Usuario:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def validar_usuario(self, nombre_usuario):
        """Valida que el nombre de usuario tenga al menos 3 caracteres"""
        return len(nombre_usuario) >= 3

    def validar_contraseña(self, contraseña):
        """Valida que la contraseña tenga al menos 6 caracteres"""
        return len(contraseña) >= 6

    def validar_correo(self, correo):
        """Valida que el correo tenga el formato adecuado"""
        return bool(re.match(r"[^@]+@[^@]+\.[^@]+", correo))

    def registrar_usuario(self, nombre_usuario, contraseña, correo):
        """Registra un nuevo usuario en la base de datos"""
        if not self.validar_usuario(nombre_usuario):
            print("El nombre de usuario debe tener al menos 3 caracteres.")
            return False
        if not self.validar_contraseña(contraseña):
            print("La contraseña debe tener al menos 6 caracteres.")
            return False
        if not self.validar_correo(correo):
            print("El correo no tiene un formato válido.")
            return False

        query = "INSERT INTO usuarios (nombre_usuario, contraseña, correo) VALUES (%s, %s, %s)"
        values = (nombre_usuario, contraseña, correo)

        resultado = self.db_manager.execute_query(query, values)

        if resultado is True:  # Solo imprimir si la consulta fue exitosa
            limpiar()
            print("Usuario registrado exitosamente.")
            

    def autenticar_usuario(self, nombre_usuario, contraseña):
        """Autentica un usuario mediante nombre y contraseña"""
        query = "SELECT contraseña FROM usuarios WHERE nombre_usuario = %s"
        result = self.db_manager.execute_query(query, (nombre_usuario,))
        if result and result[0][0] == contraseña:
            return True
        return False

