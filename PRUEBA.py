import inventory.routers as rt
from netmiko import ConnectHandler
import comandos as com


class router:
   def mostrarInterfaces():
    with ConnectHandler(**rt.pem_mex_1) as net_connect:
        output = net_connect.send_command(com.mostrar_interface[1])

    print(output)
