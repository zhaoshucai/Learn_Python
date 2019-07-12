import logging
logging.getLogger('kamene.runtime').setLevel(logging.ERROR) #关闭不必要的报错
from kamene.all import *

class routerping:
    def __init__(self,ip):
        self.ip = ip
        self.length = 100
        self.srcip = ''

    def make_pkt(self):
        if self.srcip:
            self.pkt = IP(des=self.ip, src=self.srcip,) / ICMP() / (b'v' * self.length)
        else:
            self.pkt = IP(des=self.ip,) / ICMP() / (b'v' * self.length)

    def one(self):
        self.make_pkt()
        result = sr1(self.pkt, timeout=1, verbose=False)
        if result:
            print(self.ip,'可达')
        else:
            print(self.ip, '不可达')

    def ping(self):
        self.make_pkt()
        for i in range(5):
            result = sr1(self.pkt, timeout=1, verbose=False)
            if result:
                print('!', end='', flush=True)
            else:
                print('.', end='', flush=True)

        print()
    def _str_(self):
        if not self.srcip:
            return '<{0} => dstip: {1}, size: {2}>'.format(self.__class__.__name__, self.ip, self.length)
        else:
            return '<{0} => srcip: {1}, dstip: {2}, size: {3}>'.format(self.__class__.__name__, self.srcip,self.ip, self.length)
class Newrouterping(routerping):
    def ping(self):
        self.make_pkt()
        for i in range(5):
            result = sr1(self.pkt, timeout=1, verbose=False)
            if result:
                print('+', end='', flush=True)
            else:
                print('?', end='', flush=True)

if __name__ == '__main__':
    ping = Netmanping('172.30.13.20')#使用类Netmanping,产生示例
    total_len = 70

    def print_new(word,s='-'):
        print('{0}{1}{2}'.format(s * int((70 - len(word))/2),word,s*int((70-len(word))/2)))
    print_new('print class')
    print(ping) #打印类
    print_new('ping one for sure reachable')
    ping.one() #Ping一个包判断可达性
    print_new('ping five')
    ping.ping() #模拟正常ping程序ping五个包，'!'标识通，'.'表示不通
    print_new('set payload lenth')
    ping.length = 200 #设置负载长度
    print(ping) #打印类
    ping.ping() #使用修改长度的包进行ping测试
    print_new('set ping src ip address')
    ping.srcip = '172.31.1.31' #修改源IP地址
    print(ping) #打印类
    ping.ping() #使用修改长度又修改源的包进行ping测试
    print_new('new class Newping','=')
    newping = Newping('172.31.1.254') #使用新的类Newping(通过集成Netmanping类产生)产生实例!
    newping.length = 300
    print(newping) #打印类
    newping.ping() #Newping类自定义过ping()这个方法，'+'表示通，'?'表示不通
