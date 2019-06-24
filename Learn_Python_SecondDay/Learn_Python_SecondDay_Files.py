# 1
# print('QYTANG'+'\''+'day'+'\000'+'2014'+'-'+'9'+'-'+'28')


# 2
# word = 'scallywag'
# sub_word = word[2:6]
# print(sub_word)


# 3
# word = "Python"
# sub_word = word[1:6]+str('-')+word[0]+str('y')
# print(sub_word)


# 4
# department1 = 'Security'
# department2 = 'Python'
# depart1_m = 'cq_bomb'
# depart2_m = 'qinke'
# COURSE_FEES_SEC = 456789.12456
# COURSE_FEES_Python = 1234.3456
#
# line1 = 'Department1 Name:%-10s Manager:%-10s COURSE_FEES:%-10.2f The End!' % (department1,depart1_m,\
#                                                                                COURSE_FEES_SEC)
# line2 = 'Department2 Name:%-10s Manager:%-10s COURSE_FEES:%-10.2f The End!' % (department2,depart2_m,\
#                                                                                COURSE_FEES_Python)
#
# line1 = 'Department1 Name:{0:<10} Manager:{1:<10} COURSE_FEES:{2:<10.2f} The End!'.format(department1,depart1_m,\
#                                                                                          COURSE_FEES_SEC)
# line2 = 'Department2 Name:{0:<10} Manager:{1:<10} COURSE_FEES:{2:<10.2f} The End!'.format(department2,depart2_m,\
#                                                                                          COURSE_FEES_Python)
#
# length = len(line1)
# print('='*length)
# print(line1)
# print(line2)
# print('='*length)


5
import re
str1 = 'Port-channel1.189        192.168.189.254    YES   CONFIG     up       up'
result = re.match('\s*(\w.*\d)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(\w*)\s+(\w*)\s+(\w*)\s*',str1).groups()
print(result)
print('-'*80)
print('%-7s:%s'%('接口',result[0]))
print('%-7s:%s'%('IP地址',result[1]))
print('%-7s:%s'%('状态',result[4]))

