import sys

n = int(sys.stdin.readline().rstrip())

result = []
for i in range(n):
    input_str = sys.stdin.readline().rstrip().split()
    input_result = ""
    for val in input_str[1]:
          input_result += val*int(input_str[0])

    result.append(input_result)

for val in result:
    print(val)
