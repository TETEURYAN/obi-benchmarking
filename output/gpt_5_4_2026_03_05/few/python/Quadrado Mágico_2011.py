import sys

data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit()

n = data[0]
idx = 1

target = 0
col_sums = [0] * n
diag1 = 0
diag2 = 0
seen = set()
limit = n * n

for i in range(n):
    row_sum = 0
    base = i * n
    for j in range(n):
        x = data[idx]
        idx += 1

        if x < 1 or x > limit or x in seen:
            print(0)
            sys.exit()
        seen.add(x)

        row_sum += x
        col_sums[j] += x
        if i == j:
            diag1 += x
        if i + j == n - 1:
            diag2 += x

    if i == 0:
        target = row_sum
    elif row_sum != target:
        print(0)
        sys.exit()

if len(seen) != limit or diag1 != target or diag2 != target:
    print(0)
    sys.exit()

for s in col_sums:
    if s != target:
        print(0)
        sys.exit()

print(target)