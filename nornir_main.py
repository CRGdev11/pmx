from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_cli
import dispositivo as disp

nr = InitNornir(
    config_file="config.yaml", dry_run=True
)

results = nr.run(
    task = disp.dispositivo.mostrar_interfaces
)

print_result(results)

