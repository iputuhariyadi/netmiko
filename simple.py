from netmiko import ConnectHandler
net_connect = ConnectHandler(
    device_type="cisco_ios",
    host="core.ubg.local",
    username="putu",
    password="cisco"
)
print(net_connect.find_prompt())
net_connect.disconnect()
