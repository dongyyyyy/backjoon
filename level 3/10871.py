import sys
n,x =  sys.stdin.readline().rstrip().split()
n,x = int(n),int(x)

num = sys.stdin.readline().rstrip().split()
num = list(map(int,num))


result = []
for i in range(n):
    if(num[i]<x):
        result.append(num[i])

for i in range(len(result)):
    print('{} '.format(result[i]),end='')
