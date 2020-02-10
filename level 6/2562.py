import sys

max = 0
index = 0
for i in range(9):
    number = int(sys.stdin.readline().rstrip())
    if number > max:
        max,index = number,i+1

print(max)
print(index,end='')