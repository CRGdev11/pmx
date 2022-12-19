import inventory.routers as rt
from netmiko import ConnectHandler
from getpass import getpass

class router:
   def mostrarInterfaces():
    mostrar_interfaz = "show interface brief"

    # ConnectHandler(**rt.pem_mex_1) as net_connect:
    #    output = net_connect.send_command(mostrar_interfaz)

    print(mostrar_interfaz)

router.mostrarInterfaces()
