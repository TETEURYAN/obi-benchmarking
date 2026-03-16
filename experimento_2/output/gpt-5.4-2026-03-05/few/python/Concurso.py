import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n, k = data[0], data[1]
a = data[2:2 + n]

a.sort(reverse=True)

if k == 0:
    print(101)
else:
    print(a[k - 1])