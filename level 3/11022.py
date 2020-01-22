import sys
n = int(sys.stdin.readline().rstrip())


for i in range(1,n+1):
    a,b = sys.stdin.readline().rstrip().split()
    a,b = int(a),int(b)
    print("Case #{}: {} + {} = {}".format(i,a,b,a+b))