import sys
import math
num = int(sys.stdin.readline().rstrip())

line = 1
tmp = num

while True:
    tmp -= 1*line
    if(tmp <=0):
        break
    line += 1

top_point = 0

top_point = line//2*1 +1

for i in range(1,math.ceil(line/2)): # math.ceil : 올림 / math.floor : 내림  math.round : 반올림
    top_point += i * 4

tmp = abs(num - top_point)

if tmp == 0:
    print(str(1)+"/"+str(line))
else:
    print(str(1+tmp)+"/"+str(line-tmp))

