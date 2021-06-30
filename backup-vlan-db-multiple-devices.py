from netmiko import ConnectHandler, file_transfer
import inventory
import time

def backupVLAN(backupfilename):
    source_file = "vlan.dat"
    dest_file = f"backup/{backupfilename}.vlan.dat"
    direction = "get"
    file_system = "flash:"

    transfer_dict = file_transfer(
       net_connect,
       source_file=source_file,
       dest_file=dest_file,
       file_system=file_system,
       direction=direction,
       overwrite_file=True,
    )
    return transfer_dict

for device in (inventory.sw1, inventory.sw2, inventory.sw3):
    net_connect = ConnectHandler(**device)
    hostname = net_connect.find_prompt()[:-1]
    backuptime = time.strftime("%d-%m-%Y_%H-%M-%S") 
    backupfilename = f"{hostname}-{device['ip']}_{backuptime}" 

    result = backupVLAN(backupfilename)
    if result['file_exists'] and result['file_transferred'] and result['file_verified']:
        print(f"Backup vlan database dari device {hostname} dengan IP {device['ip']} SUKSES pada {backuptime}.")
    else:
        print(f"Backup vlan database dari device {hostname} dengan IP {device['ip']} GAGAL dilakukan!.")

    net_connect.disconnect()
