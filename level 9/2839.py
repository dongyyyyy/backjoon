import sys

num = int(sys.stdin.readline().rstrip())

result = 0

while True:
    if num % 5 != 0: # 5로 나누었을 경우 0이 되는 경우에 남은 것 모두 5로 카운트하면 되기에 우선적으로 3으로 나눌 수 있는 만큼 나눈다.
        num -=3 # 3을 뺏기에 -3
        if num < 0: # 만약 3을 뺏을때 입력값이 0보다 작은 경우 초과되는 것이기에
            result = -1 # 불가함
            break
        result += 1 # 그 외의 경우에는 횟수 증가
    elif num % 5 == 0: # 5로 나누어 떨어질 경우 몫을 더한 후 반복문 탈출
        result += num //5
        break
    elif num % 5 != 0 and num % 3 != 0: # 무엇으로 나눌지라도 나머지 값을 0으로 가지지 않을 경우에는 나눌 수 없는 경우기에 바로 종료
        result = -1
        break

print(result)