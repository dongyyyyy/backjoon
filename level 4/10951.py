import sys

while True:
    try:
        a,b = map(int,sys.stdin.readline().rstrip().split())
        if((a < 10 and a > 0) and (b < 10 and b > 0)):
            print(a+b)
        else:
            break
    except:
        break