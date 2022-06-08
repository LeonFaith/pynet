import re

def get_log(file):
    with open('/home/lwang/Python-netmiko-class/pynet/cisco_show_version.txt', 'r') as f:
        log_content = f.read()
        log_content = log_content.replace('\r\n', '\n')
        return log_content


if __name__ == '__main__':
    log = get_log('version.log')
    

    software_re = re.compile(r'ROM:\s+(.*)')
    software_re_search = software_re.search(log)
    if software_re_search:
        ver = software_re_search.group(1)
        print(ver)


