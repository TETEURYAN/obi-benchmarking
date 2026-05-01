A, B, C = map(int, input().split())
sides = sorted([A, B, C])
a, b, c = sides

if a + b <= c:
    print('n')
else:
    if a*a + b*b == c*c:
        print('r')
    elif a*a + b*b > c*c:
        print('a')
    else:
        print('o')