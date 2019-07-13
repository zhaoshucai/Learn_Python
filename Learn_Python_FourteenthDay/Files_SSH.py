import paramiko

def login_ssh (ip, username, password, port = 22, cmd = 'ip address print'):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port = port , username = username, password = password, timeout=5, compress=True)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    return stdout.read().decode()


if __name__ == '__main__':
    print(login_ssh('172.30.13.1', 'admin', 'asiafort@ro'))