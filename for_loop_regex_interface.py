import re


def get_log(interface_description):
    with open('/home/lwang/Python-netmiko-class/pynet/cisco_show_interface_description.txt', 'r') as f:
        log_content = f.read()
        log_content = log_content.replace('\r\n', '\n')
        return log_content


#def get_intf_text:
#    pass


if __name__ == '__main__':
    log = get_log('interface_description.log')
#    software_re = re.compile(r'Gi\d+/\d+/\d+\s+\S+\s+\S+\s+\n', re.S)
#    software_re_search = software_re.search(log)
    intf_pattern = r'Gi\d+/\d+/\d+\s+\S+\s+\S+\s+'
    intf_match_list = re.findall(intf_pattern, log)
    for intf in intf_match_list:
        print(intf)



#    if software_re_search: 
#        intf = software_re_search.group()
#        print(intf)
    
    

