import sys

result = int(1)
count_number = [0 for i in range(10)]
for i in range(3):
    input_num = int(sys.stdin.readline().rstrip())
    result *= int(input_num)
while(True):
    if (result // 10) > 0 :
        count_number[int(result%10)] += 1
        result = result // 10
    else:
        count_number[int(result)] += 1
        break

for i in count_number:
    print(i)

