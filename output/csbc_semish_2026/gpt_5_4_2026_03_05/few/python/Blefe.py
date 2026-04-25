import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n, m = data[0], data[1]
A = data[2:2 + n]
B = data[2 + n:2 + n + m]

Aset = set(A)
present = set()

for x in B:
    if x in Aset:
        present.add(x)
        continue

    valid = False
    for y in present:
        if x - y in present:
            valid = True
            break

    if not valid:
        print(x)
        sys.exit()

    present.add(x)

print("sim")