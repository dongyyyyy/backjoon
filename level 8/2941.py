import sys

list_alpha = ['c=','c-','dz=','d-','lj','nj','s=','z=']

input_str = str(sys.stdin.readline().rstrip())

count = 0
for val in list_alpha:
    index = input_str.count(val) # 일치하는 문자열이 몇개가 있는지 확인
    input_str = input_str.replace(val," ") # 일치하는 문자열 제거
    count += index # 일치하는 문자열 수만큼 증가

for val in input_str:
    if val != ' ':
        count += 1


print(count)