from getpass import getpass

class inicioSesion():

    def inicio_sesion(self):
        self.inicio_sesion = input(" ¿Quieres iniciar sesion? y/n ")
        
    def obtener_usuario(self):
        self.usuario = input("\n introduzca el usuario: ")
        print(self.usuario)

    def obtener_contrasena(self):
        self.contrasena = getpass("\n introduzca la contrasena: ")
        print(self.contrasena)

autenticacion = inicioSesion()
#autenticacion.inicio_sesion()
#autenticacion.obtener_usuario()
#autenticacion.obtener_contrasena()
