import inventory.routers as rt
from netmiko import ConnectHandler

comando = "show ip interface brief"

class router:
   def mostrarInterfaces():
    mostrar_interfaz = "show interface brief"
    with ConnectHandler(**rt.pem_mex_1) as net_connect:
        output = net_connect.send_command(comando)

    print(mostrar_interfaz)

router.mostrarInterfaces()