import sys

data = list(map(int, sys.stdin.read().split()))
a, b, c, d = data[:4]

ans = min(
    abs((a + b) - (c + d)),
    abs((a + c) - (b + d)),
    abs((a + d) - (b + c)),
)

print(ans)