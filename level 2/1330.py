#두 수 비교하기

A,B = input().split()
A,B = int(A),int(B)

if(A>B):
    print('>')
elif(A<B):
    print('<')
else:
    print('==')