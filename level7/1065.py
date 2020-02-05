import sys

def solve2(number):
    dif = []
    if isinstance(number,int):
        return True
    if len(number) <= 2:
        return True
    for i in range(len(number)-1):
        dif.append(number[i+1]-number[i])
    for i in range(len(dif)-1):
        if dif[i] != dif[i+1]:
            return False
    return True

def solve(num):
    number = []
    if num // 10 >= 1:
        number.append(num % 10)
        new_number = solve(num//10)
        if isinstance(new_number,int):
            number.append(new_number)
        else:
            for j in new_number:
                number.append(j)
    else:
        return num
    return number


if __name__ == '__main__':
    input_num = int(sys.stdin.readline().rstrip())
    count = 0
    for i in range(1,input_num+1):
        if solve2(solve(i)) == True:
            count+=1

    print(count)