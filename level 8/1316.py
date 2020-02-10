import sys

n = int(sys.stdin.readline().rstrip())

count = 0
for i in range(n):
    input_str = str(sys.stdin.readline().rstrip())
    input_str = input_str.lower() # 소문자로 변환
    is_True = True
    for j in range(97,123): # 'a' ~ 'z'
        find_ch = chr(j) # 정수값을 아스키코드를 활용하여 문자로 표현
        find_count = input_str.count(find_ch) # 해당 문자열에 문자가 몇개가 있는지를 확인
        find_idx = input_str.find(find_ch) # 문자열에서 문자가 등장하는 첫번째 index 확인
        if input_str[find_idx:find_idx+find_count] != find_ch*find_count: # 그룹인지 확인
            is_True = False
    if is_True == True:
        count += 1

print(count)
