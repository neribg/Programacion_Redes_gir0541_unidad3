'''
    Nombre: Victor Manuel Ramirez Reyes
    Fecha: 06/12/2023
    Laboratorio: 2.2

'''
from netmiko import ConnectHandler

sshCli = ConnectHandler(
    device_type='cisco_ios',
    host='10.10.2.48',
    port=22,
    username = 'developer',
    password = 'C1sco12345',
)

salida = sshCli.send_command('show ip int brief')
print(salida)
