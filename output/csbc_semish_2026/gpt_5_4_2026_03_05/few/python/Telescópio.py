import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

A = int(data[0])
N = int(data[1])

need = 40000000
count = 0

for i in range(N):
    F = int(data[2 + i])
    if F * A >= need:
        count += 1

print(count)