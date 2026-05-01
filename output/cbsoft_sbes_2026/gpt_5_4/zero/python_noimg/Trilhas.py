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

    up_forward = 0
    for i in range(m - 1):
        if h[i + 1] > h[i]:
            up_forward += h[i + 1] - h[i]

    effort = min(up_forward, h[0] - h[-1] + up_forward)

    if best_effort is None or effort < best_effort:
        best_effort = effort
        best_id = trail_id

print(best_id)