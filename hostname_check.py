from netmiko import ConnectHandler
import json

cisco_9500 = {
    'device_type': 'cisco_ios',
    'host':   'IP_ADDRESS',
    'username': 'USERNAME',
    'password': 'PASSWORD',
}

net_connect = ConnectHandler(**cisco_9500)
output = net_connect.send_command('show ver', use_textfsm=True) #this outputs my stuff in a list

output_json = json.dumps(output, indent=2) #converts my python dictionary into json format / makes it pretty
print(output_json) #print out to check

for item in output:
	host_name = f"{item['hostname']}"

print("Hostname is: " + host_name)
