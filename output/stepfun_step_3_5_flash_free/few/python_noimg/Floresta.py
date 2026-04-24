import sys

def count_divisors(n):
    if n == 1:
        return 1
    d = 1
    i = 3
    while i * i <= n:
        cnt = 0
        while n % i == 0:
            cnt += 1
            n //= i
        d *= (cnt + 1)
        i += 2
    if n > 1:
        d *= 2
    return d

data = sys.stdin.read().split()
if not data:
    exit()
N = int(data[0])
M = 2 * N - 1
d = count_divisors(M)
print((d - 1) // 2)