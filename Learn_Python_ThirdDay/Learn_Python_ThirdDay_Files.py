# 1
import re
str1 = ' 166    54a2.74f7.0326    DYNAMIC     Gi1/0/11'
result = re.match('\s*(\d{1,3})\s+(\w[0-9a-fA-F]{2,3}\.\w[0-9a-fA-F]{2,3}\.\
\w[0-9a-fA-F]{2,3})\s+(\w*)\s+(\w*\/\d{1,2}\/\d{1,2})\s*',str1).groups()
print(result)
##方法一、
# # print('VLAN ID:{0:<10}' '\n'\
# #       'MAC:{1:<10}' '\n'\
# #       'Type:{2:<10}' '\n'\
# #       'Interface:{3:<10}'\
# #          .format(result[0],\
# #                  result[1],\
# #                  result[2],\
# #                  result[3]))
#方法二、
print('='*50)
print('%-10s: %s'%('VLAN ID',result[0]))
print('%-10s: %s'%('MAC',result[1]))
print('%-10s: %s'%('Type',result[2]))
print('%-10s: %s'%('Interface',result[3]))


# 2
# import re
# str1 = 'TCP server 172.16.1.101:443 localserver 172.16.66.1:53710 idle 0:01:09 bytes 27575949 flags UIO'
# result = re.match('\s*(\w[A-Z]{0,2})\s+\w*\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\:\d{1,3})\s\w*\s+(\d{1,3}\.\d\
# {1,3}\.\d{1,3}\.\d{1,3}\:\d{1,6})\s+\w*\s+(\d{1,2})\:(\d{1,2})\:(\d{1,2})\s\w*\s+(\d*)\s\w*\s+(\w*)\s*',str1).groups()
# ide1 = (result[3]+'小时'+result[4]+'分钟'+result[5]+'秒')
# print(result)
# print('='*50)
# print('%-10s: %s'%('protocol',result[0]))
# print('%-10s: %s'%('server',result[1]))
# print('%-10s: %s'%('locaserver',result[2]))
# print('%-10s: %s'%('idle',ide1))
# print('%-10s: %s'%('bytes',result[6]))
# print('%-10s: %s'%('flgs',result[7]))