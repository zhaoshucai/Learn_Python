import sqlite3
import os
#将字典写入SQLite数据库
homework_dict = [{'姓名':'学员1','年龄':37,'作业数':1},
                 {'姓名':'学员2','年龄':38,'作业数':9},
                 {'姓名':'学员3','年龄':31,'作业数':7}]
#链接数据库
if os.path.exists('homework.sqlite'):
    os.remove('homework.sqlite')

conn = sqlite3.connect('homework.sqlite')
cursor = conn.cursor()
#执行创建表格任务
cursor.execute('create table homework_info (学员姓名 varchar(40),学员年龄 int,学员作业数 int)')
#读取字典，将数据写入数据库
for teacher in homework_dict:
    name = teacher['姓名']
    age = teacher['年龄']
    homework = teacher['作业数']
    cursor.execute('insert into homework_info values (?,?,?)',(name, age, homework))

conn.commit()