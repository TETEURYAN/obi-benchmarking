A = int(input())
B = int(input())
C = int(input())

dist_ab = B - A
dist_bc = C - B

if dist_ab < dist_bc:
    print(1)
elif dist_ab > dist_bc:
    print(-1)
else:
    print(0)