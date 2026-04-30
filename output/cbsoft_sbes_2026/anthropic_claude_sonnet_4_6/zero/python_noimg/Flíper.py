P, R = map(int, input().split())

if P == 1 and R == 1:
    print('A')
elif P == 1 and R == 0:
    print('B')
elif P == 0 and R == 1:
    print('A')
else:  # P == 0 and R == 0
    print('C')