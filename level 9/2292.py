import sys

n = int(sys.stdin.readline().rstrip()) # 1(1*1) -> 6(1*6) -> 12(2*6) -> 18(3*6) -> 24(4*6) -> ...(n*6)

result = 1
max = 1
tmp = 1
while True:
        if(max >= n):
            break
        max += 6*(result)
        result += 1

print(result)