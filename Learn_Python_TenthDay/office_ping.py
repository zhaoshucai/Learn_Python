import logging

logging.getLogger('kamene,runtime').setLevel(logging.ERROR)  #关闭不必要的报错
from kamene.all import *

def router_ping(ip):
    ping_pkt = IP(dst=ip,ttl=1) / ICMP()    #制造一个ping包
    ping_result = sr1(ping_pkt,timeout = 2 , verbose = False)    #ping并且把结果复制给ping_result
    if ping_result:
        return ip, True
if __name__ == '__main__':
    print(router_ping('172.30.13.1'))
