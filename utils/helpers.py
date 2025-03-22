import os

def limpiar():
    """
    Limpia la pantalla de la consola.
    """
    os.system('cls' if os.name == 'nt' else 'clear')