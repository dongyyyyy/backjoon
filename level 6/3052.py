import sys

result = [0 for i in range(42)]

for i in range(10):
    input_num = int(sys.stdin.readline().rstrip())
    input_result = input_num % 42
    result[int(input_result)] +=1


answer = 0
for i in result:
    if i != 0:
        answer +=1

print(answer)