import sys

n = int(sys.stdin.readline().rstrip())

result = [0 for i in range(n)]

for i in range(n):
    input_list = list(map(int,sys.stdin.readline().rstrip().split()))
    mean = 0
    for j in range(1,input_list[0]+1):
        mean += input_list[j]
    mean /= input_list[0]
    number_student = 0
    for j in range(1,input_list[0]+1):
        if input_list[j] > mean:
            number_student += 1
    result[int(i)] = number_student/input_list[0]*100

for i in range(n):
    print("{:.3f}%".format(result[int(i)]))

