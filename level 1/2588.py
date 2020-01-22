## 곱셈 연산

A = int(input())
B = int(input())
count = 0;
newB = B
sum = 0
while(1):
    if(newB//10 != 0):
        count+=1
    else:
        break
    newB /=10


for i in range(count+1):
    temp = A*(B%10)
    print(temp)
    sum += temp*pow(10,i)
    B //= 10

print(sum)
