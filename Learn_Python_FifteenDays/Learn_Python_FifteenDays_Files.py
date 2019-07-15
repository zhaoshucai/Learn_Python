import sqlite3
import os

homework_dict = [{'姓名':'学员1','年龄':37,'作业数':1},
                 {'姓名':'学员2','年龄':38,'作业数':9},
                 {'姓名':'学员3','年龄':39,'作业数':7}]

if os.path.exists('homework.sqlite'):
    os.remove('homework_dict')

conn = sqlite3.connect('homework_dict')
cursor = conn.cursor()

cursor.execute('create table homework_info (姓名 varchar(40),年龄 int,作业数 int)')

for teacher in homework_dict:
    name = teacher['姓名']
    age = teacher['年龄']
    homework = teacher['作业数']
    cursor.execute('insert into homework_info values (?,?,?)',(name, age, homework))

conn.commit()