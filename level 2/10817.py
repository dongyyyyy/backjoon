# 세 수
A,B,C = input().split()
A,B,C = int(A),int(B),int(C)

if(A>B):
    if(A > C):
        first = A
        if(C > B):
            second = C
            third = B
        else:
            second = B
            third = C
    else:
        first = C
        second = A
        third = B
else:
    if(B > C):
        first = B
        if(C > A):
            second = C
            third = A
        else:
            second = A
            third = C
    else:
        first = C
        second = B
        thrid = A
print(second)