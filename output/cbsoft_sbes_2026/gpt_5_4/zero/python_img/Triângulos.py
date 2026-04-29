a, b, c = map(int, input().split())
x, y, z = sorted([a, b, c])

if x + y <= z:
    print('n')
else:
    s = x * x + y * y
    z2 = z * z
    if s == z2:
        print('r')
    elif s > z2:
        print('a')
    else:
        print('o')