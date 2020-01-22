# 알람시계
h , m = input().split()

h, m = int(h),int(m)

temp = m - 45

if(temp < 0):
    if (h == 0):
        h = 24 - 1
    else:
        h = h - 1
    m = 60 + temp
else:
    m = m - 45

if(h >= 24):
    h = h - 24


print(h,m)
