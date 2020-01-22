# 빠른 A+B

import sys

n = int(sys.stdin.readline().rstrip())


for i in range(n):
    a, b = sys.stdin.readline().rstrip().split()
    a, b = int(a), int(b)
    print(a+b)