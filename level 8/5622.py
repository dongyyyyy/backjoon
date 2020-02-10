import sys

def switch(value):
    value = ord(value)
    if value >=65 and value <= 90: # isAlpha
        if value <= 67: #A,B,C
            return 3
        elif value <= 70: #D,E,F
            return 4
        elif value <= 73: #G,H,I
            return 5
        elif value <= 76: #J,K,L
            return 6
        elif value <= 79: # M,N,O
            return 7
        elif value <= 83: #P,Q,R,S
            return 8
        elif value <= 86: #T,U,V
            return 9
        else: # W,X,Y,Z
            return 10
    else: # option
        return 11

number = str(sys.stdin.readline().rstrip())
number = number.upper()
result = 0
for val in number:
    result += switch(val)

print(result)
