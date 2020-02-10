import sys

n = int(sys.stdin.readline().rstrip())

result_list = [0 for i in range(n)]
for i in range(n):
    input_char = sys.stdin.readline().rstrip()
    input_result = 0
    add_num = 1
    for j in input_char:
        if(j == 'O'):
            input_result += add_num
            add_num += 1
        else:
            add_num = 1
    result_list[int(i)] = input_result

for i in result_list:
    print(i)