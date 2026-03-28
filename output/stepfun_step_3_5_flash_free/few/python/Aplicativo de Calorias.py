import sys

E1, E2, E3, X = map(int, sys.stdin.read().split())
if E2 - E1 <= X:
    print(E2)
else:
    print(E3)