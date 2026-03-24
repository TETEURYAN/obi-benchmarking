import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n = data[0]
idx = 1

fact = 1
for i in range(2, n + 1):
    fact *= i

total_xor = [0] * n
for first in range(1, n + 1):
    block = fact // n
    for pos in range(n):
        total_xor[pos] ^= first if ((block & 1) and pos == 0) else 0

for pos in range(1, n):
    total_xor[pos] = total_xor[0]
total_xor[0] = 0
for v in range(1, n + 1):
    total_xor[0] ^= v

missing = total_xor[:]

for _ in range(fact - 1):
    for pos in range(n):
        missing[pos] ^= data[idx]
        idx += 1

print(*missing)