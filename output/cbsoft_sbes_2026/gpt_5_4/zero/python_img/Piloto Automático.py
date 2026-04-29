A = int(input())
B = int(input())
C = int(input())

d1 = B - A
d2 = C - B

if d1 < d2:
    print(1)
elif d1 > d2:
    print(-1)
else:
    print(0)