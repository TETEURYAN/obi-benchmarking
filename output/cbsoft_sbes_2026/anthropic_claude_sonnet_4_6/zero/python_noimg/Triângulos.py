a, b, c = sorted(map(int, input().split()))

if a + b <= c:
    print('n')
else:
    if a*a + b*b == c*c:
        print('r')
    elif a*a + b*b > c*c:
        print('a')
    else:
        print('o')