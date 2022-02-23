import string
import random
import glob
import os
from datetime import datetime
n = 10000 # 몇개?
arr = []
inarr = []
result = []
i = 0

def ranTel() :
    result=""
    for i in range(8):
        result += random.choice(string.digits)

    return result

for filename in glob.glob('db/*.txt'):
   with open(os.path.join(os.getcwd(), filename), 'r') as f:
        lines = f.readlines()
        lines = [line.rstrip('\n') for line in lines]
        lines = [line.lstrip('010') for line in lines]
        inarr = inarr + lines

current_time = datetime.now()
timeinput = f'{current_time.year}년{current_time.month}월{current_time.day}일{current_time.hour}시{current_time.minute}분{current_time.second}초'
print(timeinput)

while True:
    aa = ranTel()
    telint = int(aa)
    if 20000000 < telint <59000000 or 62000000 < telint < 99999999:
        if aa not in inarr:
            if aa not in arr:
                arr.append(aa)
                result.append("010"+aa)
                i= i+1
    if i == n:
        break

aaa = str(n)

with open('db/'+timeinput+aaa+'개.txt','w',encoding='UTF-8') as f:
    for num in result:
        f.write(num+'\n')
