import paramiko
import re
import hashlib
import sqlite3

def AR1_ssh(ip, username, password, cmd='ls', port=22):
    ssh = paramiko.SSHClient()
    ssh.load_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port=port, username=username, password=password, timeout=5, compress=True)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    x= stdout.read().decode()
    return x

def get_config_md5(ip, username='admin', password='admin'):
    try:
        device_config_raw = AR1_ssh(ip, username, password, 'dis cu ')
        split_result = re.split(r'\r\nsysname \S+\r\n', device_config_raw)
        device_config = device_config_raw.replace(split_result[0], '').strip()
        m = hashlib.md5()
        m.update(device_config.encode())
        md5_value = m.hexdigest()
        return device_config, md5_value
    except Exception:
        return

device_list = ['172.30.13.55']
username = 'admin'
password = 'admin'

def write_config_md5_to_db():
    conn = sqlite3.connect('AR1.sqlite')
    cursor = conn.cursor()
    for device in device_list:
        confing_and_md5 = get_config_md5(device, username, password)
        cursor.execute('select * from config_md5 where ip=?', (device,))
        md5_result = cursor.fetchall()
        if not md5_result:
            cursor.execute('insert into config_md5(ip, config, md5) values (?,?,?)',(device,
                                                                                    confing_and_md5[0],
                                                                                    confing_and_md5[1]))
            conn.commit()
        else:
            if confing_and_md5[1] != md5_result[0][2]:
                cursor.execute('update config_md5 set config=?, md5=? where ip=?',(confing_and_md5[0],
                                                                                   confing_and_md5[1],
                                                                                   device))
                conn.commit()
            else:
                continue
    cursor.execute('select * from config_md5')
    all_result = cursor.fetchall()
    for x in all_result:
        print(x[0], x[2])
    conn.close()

if __name__ == '__main__':
    import os
    if os.path.exists('AR1.sqlite'):
        os.remove('AR1.sqlite')

    conn = sqlite3.connect('AR1.sqlite')
    cursor = conn.cursor()
#执行创建表的任务
    cursor.execute('create table config_md5 (ip varchar(40) , config varchar (99999), md5 varchar (1000))')
    conn.commit()
    conn.close()
    write_config_md5_to_db()
