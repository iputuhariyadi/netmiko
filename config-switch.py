from netmiko import ConnectHandler
sw1 = {
   "device_type": "cisco_ios",
   "host": "sw1.ubg.local",
   "username": "putu",
   "password": "cisco"
}
sw2 = {
   "device_type": "cisco_ios",
   "host": "sw2.ubg.local",
   "username": "putu",
   "password": "cisco"
}
sw3 = {
   "device_type": "cisco_ios",
   "host": "sw3.ubg.local",
   "username": "putu",
   "password": "cisco"
}
cfg_vlan = "vlan-database.txt"
cfg_file = "config-management-switch.txt"
for device in (sw1, sw2, sw3):
    net_connect = ConnectHandler(**device)
    output = net_connect.send_config_from_file(cfg_vlan, config_mode_command="vlan database")
    output += net_connect.send_config_from_file(cfg_file)
    output += net_connect.save_config()
    print(output)
    print("*"*30)
    net_connect.disconnect()
