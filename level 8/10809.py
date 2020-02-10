import sys

result = [-1 for i in range(26)]

s = str(sys.stdin.readline().rstrip())

for idx,value in enumerate(s):
    ch = ord(value)-97
    if result[ch] == -1:
        result[ch] = idx

for i in result:
    print("%d "%i,end="")