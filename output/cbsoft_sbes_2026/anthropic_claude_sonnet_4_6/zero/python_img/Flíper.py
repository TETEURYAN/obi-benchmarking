P, R = map(int, input().split())

if P == 1:
    print('B' if R == 0 else 'C')
else:
    print('A' if R == 0 else 'B')