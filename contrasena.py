from getpass import getpass

class inicioSesion():
    usuario = None

    def inicio_sesion(self):
        self.inicio_sesion = input(" ¿Quieres iniciar sesion? y/n ")

    def obtener_usuario(self):
        self.usuario = getpass("\n introduzca el usuario: ")
        print(self.usuario)

    def obtener_contrasena(self):
        self.contrasena = getpass("\n introduzca la contrasena: ")

autenticacion = inicioSesion
autenticacion.obtener_usuario()