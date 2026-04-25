import sys

data = sys.stdin.read().split()
if not data:
    exit()

P1, C1, P2, C2 = map(int, data)
prod_left = P1 * C1
prod_right = P2 * C2

if prod_left == prod_right:
    print(0)
elif prod_left > prod_right:
    print(-1)
else:
    print(1)