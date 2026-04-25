import sys

data = sys.stdin.read().split()
if not data:
    exit()

A = int(data[0])
B = int(data[1])

def isqrt(n):
    x = int(n ** 0.5)
    while (x + 1) * (x + 1) <= n:
        x += 1
    while x * x > n:
        x -= 1
    return x

def count_leq(limit):
    r = isqrt(isqrt(limit))
    while (r + 1) ** 6 <= limit:
        r += 1
    while r ** 6 > limit:
        r -= 1
    return r

print(count_leq(B) - count_leq(A - 1))