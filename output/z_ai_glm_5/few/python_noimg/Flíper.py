
import sys

P, R = map(int, sys.stdin.read().split())

if P == 0:
    print('C')
elif R == 0:
    print('B')
else:
    print('A')
