import sys

input_str = str(sys.stdin.readline().rstrip())

input_str = input_str.split()

for i in range(len(input_str)):
    val = list(input_str[i])
    val.reverse()
    input_str[i] = ''.join(val)

if input_str[0] > input_str[1]:
    print(input_str[0])
else:
    print(input_str[1])