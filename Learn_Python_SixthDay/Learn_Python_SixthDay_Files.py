1
import re
asa_conn = "TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247, idle 0:00:00,\
 bytes 74, flags UIO\n TCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233, \
 idle 0:00:03, bytes 334516, flags UIO"
asa_dict = {}

for conn in asa_conn.split('\n')
    re_result = re.match()
    asa_dict[] = ()
print('打印分析后的字典!\n')
print(asa_dict)

src = 'src'
src_ip = 'src_ip'
dst = 'dst'
dst_ip = 'dst_ip'
bytes_name = 'bytes'
flags = 'flags'
format_str1 =
format_str2 =
print('\n格式化打印输出\n')
for key, value in asa_dict.items():



# 2
# import re
# port_list = ['eth 1/101/1/42','eth 1/101/1/26','eth 1/101/1/23',\
#              'eth 1/101/1/7','eth 1/101/2/46','eth 1/101/1/34','eth 1/101/1/18',\
#              'eth 1/101/1/13','eth 1/101/1/32','eth 1/101/1/25','eth 1/101/1/45','eth 1/101/2/8']
#
# port_list.sort(key=lambda x: (int(re.findall(r'\d+', x)[0]),
#                               int(re.findall(r'\d+', x)[1]),
#                               int(re.findall(r'\d+', x)[2]),
#                               int(re.findall(r'\d+', x)[3])))
# print(port_list)

