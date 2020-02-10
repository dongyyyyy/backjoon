import sys

result = [0 for i in range(26)]

str = str(sys.stdin.readline().rstrip())

str = str.upper()

for val in str:
    result[ord(val)-65] += 1

max = -1
result_ptr = -1
max_count = 0
for index,val in enumerate(result):
    if(val > max):
        max = val
        result_ptr = index
        max_count = 1
    elif(val==max):
        max_count = 2
    else:
        continue


if(max_count==2):
    print("?")
else:
    print(chr(result_ptr+65))