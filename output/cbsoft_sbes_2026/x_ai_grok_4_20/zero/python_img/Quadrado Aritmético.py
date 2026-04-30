
import sys

input = sys.stdin.read
data = input().split()
N = int(data[0])
S = int(data[1])

if N == 1:
    print(S)
    sys.exit(0)

if N == 2:
    a = 23
    b = 40
    c = 9
    d = 26
    diff = S - 49
    print(a + diff, b + diff)
    print(c + diff, d + diff)
    sys.exit(0)

M = N - 1
base = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        base[i][j] = i * M - j

total = 0
for i in range(N):
    total += base[i][i]
diff = S - total

for i in range(N):
    base[i][i] += diff

used = set()
for i in range(N):
    for j in range(N):
        used.add(base[i][j])

candidates = []
val = -2 * 10**9
while len(candidates) < N * N:
    if val not in used:
        candidates.append(val)
    val += 1

idx = 0
for i in range(N):
    for j in range(N):
        if base[i][j] > 10**9 or base[i][j] < -10**9:
            base[i][j] = candidates[idx]
            idx += 1

for row in base:
    print(' '.join(map(str, row)))
