import sys

data = list(map(int, sys.stdin.read().split()))
a1, d1, a2, d2 = data

j1_desmaia = d1 != a2
j2_desmaia = d2 != a1

if not j1_desmaia and j2_desmaia:
    print(1)
elif not j2_desmaia and j1_desmaia:
    print(2)
else:
    print(-1)