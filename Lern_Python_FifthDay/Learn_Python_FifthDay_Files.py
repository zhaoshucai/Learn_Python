# 1
# import os
# import re
# route_n_result = os.popen('route -n').read()
# re_finall_result = re.findall('\s*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s',route_n_result)
# for ip in re_finall_result :
#     if ip.split('.')[-1] == '0' :
#         note = ip
#     elif ip.split('.')[-1] == '255' :
#         note = ip
#     else:
#         Gateway = ip
# print('%s:%s'%('网关地址',Gateway))

2
L1 = [4,5,7,1,3,9,0]
L2 = L1[:]
L2.sort()
for i in range(0,len(L1)) :
    print(L1[i],L2[i])