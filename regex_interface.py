import re

def get_log(interface_description):
    with open('/home/lwang/Python-netmiko-class/pynet/cisco_show_interface_description.txt', 'r') as f:
        log_content = f.read()
        log_content = log_content.replace('\r\n', '\n')
        return log_content


if __name__ == '__main__':
    log = get_log('interface_description.log')
    

    software_re = re.compile(r'(Gi\d+/\d+/\d+)',re.S)
    software_re_search = software_re.search(log)
    if software_re_search:
        interface_dp = software_re_search.group()
        print(interface_dp)
    else:
        print("error, cannot match any")

