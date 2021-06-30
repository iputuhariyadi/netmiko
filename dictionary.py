from netmiko import ConnectHandler
core = {
   "device_type": "cisco_ios",
   "host": "core.ubg.local",
   "username": "putu",
   "password": "cisco"
}
net_connect = ConnectHandler(**core)
print(net_connect.find_prompt())
net_connect.disconnect()
