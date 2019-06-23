# 随机产生IP
import random
sr1 = random.randint(1, 255)
sr2 = random.randint(1, 255)
sr3 = random.randint(1, 255)
sr4 = random.randint(1, 255)
random_ip = str(sr1)+"."+str(sr2)+"."+str(sr3)+"."+str(sr4)
print(random_ip)