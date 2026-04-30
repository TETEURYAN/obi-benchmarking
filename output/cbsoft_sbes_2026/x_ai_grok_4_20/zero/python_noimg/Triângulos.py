
a, b, c = map(int, input().split())
if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b

if a + b <= c:
    print('n')
else:
    aa = a * a
    bb = b * b
    cc = c * c
    if aa + bb == cc:
        print('r')
    elif aa + bb > cc:
        print('a')
    else:
        print('o')
