
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
A = list(map(int, data[1:]))

if N == 0:
    print(0)
    sys.exit(0)

total = sum(A)
if total > 0:
    print(total)
    sys.exit(0)

max_sum = 0
current = 0
for x in A:
    current = max(x, current + x)
    max_sum = max(max_sum, current)

if max_sum == 0:
    doubled = A + A
    max_sum = 0
    current = 0
    for x in doubled:
        current = max(x, current + x)
        max_sum = max(max_sum, current)

print(max_sum)
