from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko.tasks import netmiko_send_command, netmiko_send_config
from nornir_napalm.plugins.tasks import napalm_cli

nr = InitNornir(
  config_file = 'config.yaml', dry_run= True)

result = nr.run(task = napalm_cli, command = ['sho interface brief'])

print_result(result)
#prueba