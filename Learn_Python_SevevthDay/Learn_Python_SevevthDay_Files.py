import os
os.mkdir('test')
os.chdir('test')
qytang1 = open('qytang1','w')
qytang1.write('test file\n')
qytang1.write('this is qytang\n')
qytang1.close()
qytang2 = open('qytang2','w')
qytang2.write('test file\n')
qytang2.write('qytang python\n')
qytang2.close()
qytang3 = open('qytang3','w')
qytang3.write('test file\n')
qytang3.write('this is python\n')
qytang3.close()
os.mkdir('qytang4')
os.mkdir('qytang5')

print('文件中包含"qytang"关键字的文件为:')
for root , dirs , files in os.walk(os.getcwd(), topdown=False):
   for find_files1 in files:
       for find_files2 in (open(find_files1,'r')):
           if 'qytang' in find_files2 :
              print('',find_files1)
#完成清理工作
os.chdir('..')
for root , dirs , files in os.walk('test' , topdown=False):
    for name in files:
        os.remove(os.path.join(root,name))
    for name in dirs:
        os.rmdir(os.path.join(root,name))
os.remove('test')

