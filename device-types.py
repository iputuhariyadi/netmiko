from netmiko import ConnectHandler
net_connect = ConnectHandler(
    device_type="invalid",
    host="core.ubg.local",
    username="putu",
    password="cisco"
)
