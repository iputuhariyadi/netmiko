from netmiko import ConnectHandler
core = {
   "device_type": "cisco_ios",
   "host": "core.ubg.local",
   "username": "putu",
   "password": "cisco"
}
net_connect = ConnectHandler(**core)
output = net_connect.send_command("show ip int brief")
print(output)
net_connect.disconnect()
