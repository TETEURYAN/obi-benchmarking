import sys
P, R = map(int, sys.stdin.read().split())

if P == 1 and R == 0:
    print('B')
elif P == 1 and R == 1:
    print('A')
elif P == 0 and R == 0:
    print('C')
else:
    print('B')