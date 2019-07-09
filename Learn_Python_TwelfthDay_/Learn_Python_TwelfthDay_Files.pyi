import paramiko
import time

def router_multicmd(ip, username, password, cmd_list, sys='', wait_time=2, verbose=True):
    ssh = pe=paramiko.SSHClient() #创建SSH Client
    ssh.load_host_keys() #加载系统SSH密钥
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #添加新的SSH密钥
    ssh.connect(ip, port=22, username=username, password=password, timeout=5, compress=True) #SSH链接
    chan = ssh.invoke_shell() #激活交互式SHELL
    time.sleep(1) #等待网络设备回应
    x = chan.recv(2048).decode()
    if sys and '>' in x:
        chan.send('sys'.encode())
        chan.send(b'\n')
        chan.send(sys.encode())
        chan.send(b'\n')
        time.sleep(wait_time)
    elif not sys and '>' in x:
        print('需要配置system-view密码')
        return
    for cmd in cmd_list:
        chan.send(cmd.encode())
        chan.send(b'\n')
        time.sleep(wait_time)
        x = chan.recv(40960).decode()
        if verbose:
            print(x)
    chan.close()
    ssh.close()

if __name__ == '__main__':
    router_multicmd('172.30.13.55',
                    'admin',
                    'python123',
                    ['screen-length 0',
                     'dis cu',
                     'sys'
                     'ospf 1',
                     'area 0',
                     'network 192.168.16.0 0.0.0.255'],
                     sys='',
                     wait_time=1,
                    verbose=False
                    )
