from netmiko import ConnectHandler
from getpass import getpass
import inventory.routers as rt
import PRUEBA as pb

#contrasena = getpass()

comando = "show ip interface brief"

with ConnectHandler(**rt.pem_mex_1) as net_connect:
    output = net_connect.send_command(comando)


print("\n", output)

