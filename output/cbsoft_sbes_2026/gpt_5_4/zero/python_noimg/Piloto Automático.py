a = int(input())
b = int(input())
c = int(input())

d1 = b - a
d2 = c - b

if d1 < d2:
    print(1)
elif d1 > d2:
    print(-1)
else:
    print(0)