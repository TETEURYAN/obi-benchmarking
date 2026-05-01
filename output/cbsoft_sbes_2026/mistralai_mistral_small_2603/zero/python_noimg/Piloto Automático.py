
A = int(input())
B = int(input())
C = int(input())

dist_AB = B - A
dist_BC = C - B

if dist_AB < dist_BC:
    print(1)
elif dist_AB > dist_BC:
    print(-1)
else:
    print(0)
