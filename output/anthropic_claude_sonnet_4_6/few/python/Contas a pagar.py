import sys

data = sys.stdin.read().split()
V = int(data[0])
A = int(data[1])
F = int(data[2])
P = int(data[3])

bills = sorted([A, F, P])
count = 0
remaining = V
for bill in bills:
    if remaining >= bill:
        remaining -= bill
        count += 1
    else:
        break

print(count)