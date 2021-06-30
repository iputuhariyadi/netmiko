from netmiko import ConnectHandler
import inventory
import time

for device in (inventory.core, inventory.sw1, inventory.sw2, inventory.sw3):
    net_connect = ConnectHandler(**device)
    hostname = net_connect.find_prompt()[:-1]
    backuptime = time.strftime("%d-%m-%Y_%H-%M-%S") 
    backupfilename = f"{hostname}-{device['ip']}_{backuptime}" 
    output = net_connect.send_command("show running-config")
    file = open(f"backup/{backupfilename}.cfg", "w")
    file.write(output)
    file.close()
    net_connect.disconnect()
    print(f"Backup config dari device {hostname} dengan IP {device['ip']}")
    print(f"Sukses dibackup pada {backuptime}.")
    print("*"*50)
