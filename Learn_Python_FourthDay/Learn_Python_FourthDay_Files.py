# str1 = 'ens160: flags=4163<UP,BROADCAST,RUNNING,MULTICAST> mtu 1500 \
#               inet 172.16.66.166 netmask 255.255.255.0 broadcast 172.16.66.255\
#               inet6 fe80::250:56ff:feab:59bd prefixlen 64 scopeid 0x20<link>\
#               ether 00:50:56:ab:59:bd txqueuelen 1000 (Ethernet)\
#               RX packets 174598769 bytes 1795658527217 (1.6 TiB)\
#               RX errors 1 dropped 24662 overruns 0 frame 0\
#               TX packets 51706604 bytes 41788673420 (38.9 GiB)\
#               TX errors 0 dropped 0 overruns 0 carrier 0 collisions 0'
import os
import re
ifconfig_result = os.popen('ifconfig'+'ens160').read()
#正则表达式查找IP、掩码、广播和MAC地址
ipv4_add = re.findall(\\\,ifconfig_result)[0]
netmask = re.findall(\\\,ifconfig_result)[0]
broadcast = re.findall(\\\,ifconfig_result)[0]
mac_addr = re.findall(\\\,ifconfig_result)[0]
#格式化字符串
format_string =\\\
#打印结果
print(format_string.format(\\\))
print(format_string.format(\\\))
print(format_string.format(\\\))
print(format_string.format(\\\))
#产生网关的IP地址


#打印网关IP地址
print('\n我们假设网关IP地址为最后一位为254，因此网关IP地址为:'+ ipv4_gw +'\n')

#ping网关
ping_result = os.popen('ping' + ipv4_gw + '-c 1').read()
re_ping_result = \\\
if re_ping_result:
    print('网关可达！')
else:
    print('网关不可达！')
