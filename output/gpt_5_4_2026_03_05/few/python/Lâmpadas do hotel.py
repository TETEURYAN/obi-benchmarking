import sys

data = list(map(int, sys.stdin.read().split()))
ia, ib, fa, fb = data

da = ia ^ fa
db = ib ^ fb

if db == 0:
    print(da)
else:
    print(1 if da == 0 else 2)