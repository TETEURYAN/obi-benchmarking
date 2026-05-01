a, b, c = map(int, input().split())
x, y, z = sorted([a, b, c])

if x + y <= z:
    print('n')
else:
    s = x * x + y * y
    t = z * z
    if s > t:
        print('a')
    elif s == t:
        print('r')
    else:
        print('o')