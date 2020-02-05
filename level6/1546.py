import sys

n = int(sys.stdin.readline().rstrip())

number = list(map(int,sys.stdin.readline().rstrip().split()))

max_score = max(number)

result = 0
for i in number:
    i = i / max_score * 100
    result += i

print(result/n)