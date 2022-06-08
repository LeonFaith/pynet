from netmiko import ConnectHandler

device = {
    'host': 'cisco3.lasthop.io',
    'username': 'pyclass',
    'password': '88newclass',
    'device_type': 'cisco_ios',
    'session_log': 'my_session.txt',

}

net_connect = ConnectHandler(**device)
output = net_connect.send_command('show version')
with open ('cisco_show_version.txt', 'w') as f:
    f.write("cisco version\n\n" + output + "\n------------------------------------------------------------\n")
    



