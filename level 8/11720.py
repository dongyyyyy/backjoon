import sys

n = int(sys.stdin.readline().rstrip())

num = str(sys.stdin.readline().rstrip())

result = 0

for i in num:
    result += int(i)

print(result)