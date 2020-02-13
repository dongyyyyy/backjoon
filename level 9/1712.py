import sys

input_num = list(map(int,sys.stdin.readline().rstrip().split()))

if input_num[2] - input_num[1] <= 0 :
    print(-1)
else:
    print(int(input_num[0]/(input_num[2]-input_num[1])+1))

