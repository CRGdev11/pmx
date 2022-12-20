from getpass import getpass

class inicioSesion():
    def inicioSesion():
        inicio_sesion = input(" ¿Quieres iniciar sesion? y/n ")
        if (inicio_sesion == "Y" or "y"):
            obtenerCredenciales.credenciales()

class obtenerCredenciales():
    def credenciales():
            usuario = getpass("\n introduzca el usuario: ")
            contrasena = getpass("\n introduzca la contraseña: ")

inicioSesion.inicioSesion()