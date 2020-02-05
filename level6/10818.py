import sys

n = int(sys.stdin.readline().rstrip())

number = list(map(int,sys.stdin.readline().rstrip().split()))
max = -1000000
min = 1000000

for i in number:
    if i > max :
        max = i
    if i < min :
        min = i

print(min,max)

