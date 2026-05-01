
a, b, c = sorted(map(int, input().split()))
if a + b <= c:
    print('n')
else:
    aa, bb, cc = a*a, b*b, c*c
    if aa + bb == cc:
        print('r')
    elif aa + bb > cc:
        print('a')
    else:
        print('o')
