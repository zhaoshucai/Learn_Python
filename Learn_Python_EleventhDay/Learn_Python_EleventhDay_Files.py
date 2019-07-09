from router_ssh import router_ssh
import re
import hashlib
import time

def router_get_configer(ip, username='admin', password='asiafort@ro'):
    try:
        device_config_raw = router_ssh(ip, username, password,'ip address print')
        split_result = re.split(r'\r\n \S+\r\n', device_config_raw)
        device_config = device_config_raw.replace(split_result[0], '').strip()
        return device_config
    except Exception:
        return

def router_check_diff(ip, username='admin', password='asiafort@ro'):
    before_md5 = ''
    while True:
        device_config = router_get_configer(ip, username, password)
        m = hashlib.md5()
        m.update(device_config.encode())
        md5_value = m.hexdigest()
        print(md5_value)
        if not before_md5:
            before_md5 = md5_value
        elif before_md5 != md5_value:
            print('MD5 changed')
            break
        time.sleep(5)

if __name__ == '__main__':
    router_check_diff('172.30.13.1', username='admin', password='asiafort@ro')