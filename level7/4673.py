

def solve(number):
    result = number
    while(True):
        if number // 10 > 0 :
            result += number % 10
            number = number //10
        else:
            result += number
            break
    return result

if __name__ == '__main__':
    result = [False for i in range(10001)]
    for i in range(1,10001):
        num = solve(i)

        if(num < 10001):
            result[int(num)] = True

    for i in range(1,10001):
        if(result[i]==False):
            print(i)
