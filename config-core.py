from netmiko import ConnectHandler
core = {
   "device_type": "cisco_ios",
   "host": "core.ubg.local",
   "username": "putu",
   "password": "cisco"
}
cfg_file = "config-management-router.txt"
net_connect = ConnectHandler(**core)
output = net_connect.send_config_from_file(cfg_file)
output += net_connect.save_config()
print(output)
net_connect.disconnect()
