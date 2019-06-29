1
import re
asa_conn = "TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247, idle 0:00:00,\
 bytes 74, flags UIO\n TCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233, \
 idle 0:00:03, bytes 334516, flags UIO"
asa_list = asa_conn.split('\n')

asa_dict = {}

for conn in asa_list :
    re_result = re.match(".*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5}).*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):("
    "\d{1,5}).*bytes\s+(\d+).*flags\s+(\w*)\s*",conn).groups()
    test_key = re_result[0], re_result[1], re_result[2], re_result[3]
    test_value = re_result[4], re_result[5]
    asa_dict[test_key] = test_value

print('\n打印分析后的字典!\n')
print(asa_dict)
src = 'src'
src_ip = 'src_ip'
dst = 'dst'
dst_ip = 'dst_ip'
bytes_name = 'bytes'
flags = 'flags'
print('\n格式化打印输出\n')
print(asa_dict)
for key, value in asa_dict.items():
    print('{0:>10}{1}{2:<20}{3}{4:>10}{5}{6:<10}{7}{8:>10}{9}{10:<10}{11}{12:>10}{13}{14:<10}{15}'\
          .format('src', ':',key[0], '|','src_ip', ':',key[1], '|','dst', ':', key[2], '|','dst_ip', ':',key[3], '|'))
    print('{0:>10}{1}{2:<20}{3}{4:>10}{5}{6:<10}'.format('bytes', ':', value[0], '|', 'flags', ':', value[1]))
    print('-' * 120)

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

