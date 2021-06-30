from netmiko import ConnectHandler
core = {
   "device_type": "cisco_ios",
   "host": "core.ubg.local",
   "username": "putu",
   "password": "cisco"
}
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
for device in (core, sw1, sw2, sw3):
    net_connect = ConnectHandler(**device)
    print(net_connect.find_prompt())
    net_connect.disconnect()
