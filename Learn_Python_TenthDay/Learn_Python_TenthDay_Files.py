from router_ping import router_ping
from router_ssh import router_ssh
import re
import pprint

def router_get_if(*ips,username='admin',password='asiafort@ro'):
    device_if_dict = {}
    for ip in ips:
        if_dict = {}
        if router_ping(ip):
            for line in router_ssh(ip,username,password,'ip address print').split('\n'):
                re_relust = re.match(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d{1,2})\s+'
                                     r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+'
                                     r'([a-z]\S+\d+)\s*',line.strip())
                if re_relust:
                    if_dict[re_relust.groups()[2]] = re_relust.groups()[0]
        device_if_dict[ip] = if_dict

    return device_if_dict

if __name__ == '__main__':
    pprint.pprint(router_get_if('172.30.13.1',username='admin',password='asiafort@ro'),indet = 4)