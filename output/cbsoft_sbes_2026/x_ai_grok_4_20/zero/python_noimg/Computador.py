
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])

diff = [0] * (N + 2)
queries = []

idx = 2
for _ in range(M):
    t = int(data[idx])
    idx += 1
    if t == 3:
        i = int(data[idx])
        idx += 1
        queries.append((3, i))
    else:
        i = int(data[idx])
        v = int(data[idx + 1])
        idx += 2
        queries.append((t, i, v))

for q in queries:
    if q[0] == 3:
        continue
    t, i, v = q
    if t == 1:
        l = i
        r = min(N, i + v - 1)
        if l > r:
            continue
        diff[l] += v
        k = v - (r - l + 1)
        if k > 0:
            diff[r + 1] -= k
        diff[r + 1] -= 1
        diff[N + 1] += 1
    else:
        r = i
        l = max(1, i - v + 1)
        if l > r:
            continue
        diff[l] += (v - (i - l))
        diff[r + 1] -= (v - (i - l))
        diff[l] += 1
        diff[r + 1] -= 1
        if l > 1:
            diff[1] -= (v - (i - l) + 1)
            diff[l] += (v - (i - l) + 1)

prefix = 0
val = 0
results = []
pos = 0
for i in range(1, N + 1):
    prefix += diff[i]
    val += prefix
    while pos < len(queries) and queries[pos][0] == 3 and queries[pos][1] == i:
        results.append(str(val))
        pos += 1
    if pos >= len(queries):
        break

print('\n'.join(results))
