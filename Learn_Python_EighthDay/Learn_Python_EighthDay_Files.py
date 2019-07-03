# # 1

# import re
# import os
# import time
#
# from http.server import HTTPServer, CGIHTTPRequestHandler
# port = 80
# httpd = HTTPServer(('',port), CGIHTTPRequestHandler)
# print('Starting simple httpd on port: ' + str(httpd.server_port))
# httpd.serve_forever()
# while True:
#     netstat = os.popen('netstat -tulnp').read()
#     netstat_list = netstat.split('\n')
#     for i in netstat_list:
#         session_type = re.findall('(tcp)\s+\d+\s+\d+\s+\d{1,3}\.+\d{1,3}\.+\d{1,3}\.+\d{1,3}:(80)',i)
#         if session_type == [('tcp','80')]:
#             print('HTTP(TCP/80)服务已经被打开')
#             break
#         else:
#             print('等待1秒重新开始监控')
#             time.sleep(1)
#             continue
#         break
# if __name__ == '__main__':
#     pass


# # 2.1
list1 = ['aaa', 111, (4, 5), 2.01]
list2 = ['bbb', 333, 111, 3.14, (4, 5)]
# for i in list1:
#     if i in list2:
#         print(i,'in list1 and list2')
#     else:
#         print(i,'only in list1')
# print('\n')
# # 2.2
# def findsame(list1,list2):
#     for i in list1:
#         if i in list2:
#             print(i,'in list1 and list2')
#         else:
#             print(i,'only in list1')
# findsame(list1,list2)
#
# if __name__ == '__main__':
#     pass



# 3
import logging

logging.getLogger('kamene,runtime').setLevel(logging.ERROR)
from kamene.all import *

def qytang_ping(ip):
    ping_pkt = IP(dst=ip,ttl=1) / ICMP()
    ping_result = sr1(ping_pkt,timeout = 2 , verbose = False)
    if ping_result:
        return ip, 1
    else:
        return ip, 0
if __name__ == '__main__':
    result = qytang_ping('172.30.13.1')
    if result[1]:
        print(result[0],'网络通畅')
    else:
        print(result[0],'网络故障')
