from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_command


class dispositivo:
    hostname = None
    direccion_ipv4 = None
    SO = None
    direccion_ipv6 = None

    def alta_inventario(self):
        pass

    def mostrar_interfaces(self):
        output = netmiko_send_command,
        command_string = 'show ip interface brief'
        
        print(output)



    def mostrar_chasis(self):
        pass
    
#class router:

#class switch