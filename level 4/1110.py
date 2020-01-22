import sys

result = int(sys.stdin.readline().rstrip())
answer = result
count = 0

while True:
    if(result >= 10):
        result = (result%10)*10 + (result%10 + result //10)%10
    else:
        result = result*10 + result
    count +=1
    if(result == answer):
        break
print(count)