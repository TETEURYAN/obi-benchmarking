import sys

data = list(map(int, sys.stdin.read().split()))
p1, c1, p2, c2 = data

left = p1 * c1
right = p2 * c2

if left == right:
    print(0)
elif left > right:
    print(-1)
else:
    print(1)