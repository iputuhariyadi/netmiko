from netmiko import ConnectHandler
core = {
   "device_type": "cisco_ios",
   "host": "core.ubg.local",
   "username": "putu",
   "password": "cisco"
}
commands = ["interface FastEthernet0/0","ip address dhcp","no shutdown"]
net_connect = ConnectHandler(**core)
output = net_connect.send_config_set(commands)
output += net_connect.save_config()
print(output)
net_connect.disconnect()
