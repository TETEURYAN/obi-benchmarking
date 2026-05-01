import sys

data = list(map(int, sys.stdin.buffer.read().split()))
n = data[0]
idx = 1

best_id = 1
best_effort = None

for trail_id in range(1, n + 1):
    m = data[idx]
    idx += 1
    h = data[idx:idx + m]
    idx += m

    subida_ida = 0
    for i in range(1, m):
        if h[i] > h[i - 1]:
            subida_ida += h[i] - h[i - 1]

    subida_volta = 0
    for i in range(1, m):
        if h[i - 1] > h[i]:
            subida_volta += h[i - 1] - h[i]

    effort = min(subida_ida, subida_volta)

    if best_effort is None or effort < best_effort:
        best_effort = effort
        best_id = trail_id

print(best_id)