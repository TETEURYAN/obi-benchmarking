import sys

input_data = sys.stdin.read().split()
idx = 0
N = int(input_data[idx])
idx += 1
X = [int(input_data[idx + i]) for i in range(N)]
idx += N
Y = [int(input_data[idx + i]) for i in range(N)]

if N == 1:
    print(0)
    sys.exit()

a = [X[i] + Y[i] for i in range(N)]
b = [X[i] - Y[i] for i in range(N)]

order = sorted(range(N), key=lambda i: a[i])

INF = float('inf')

min_a_prefix = [INF] * (N + 1)
max_a_prefix = [-INF] * (N + 1)
min_b_prefix = [INF] * (N + 1)
max_b_prefix = [-INF] * (N + 1)

for i in range(1, N + 1):
    idx = order[i - 1]
    min_a_prefix[i] = min(min_a_prefix[i - 1], a[idx])
    max_a_prefix[i] = max(max_a_prefix[i - 1], a[idx])
    min_b_prefix[i] = min(min_b_prefix[i - 1], b[idx])
    max_b_prefix[i] = max(max_b_prefix[i - 1], b[idx])

suffix_min_a = [INF] * (N + 1)
suffix_max_a = [-INF] * (N + 1)
suffix_min_b = [INF] * (N + 1)
suffix_max_b = [-INF] * (N + 1)

suffix_min_a[N] = INF
suffix_max_a[N] = -INF
suffix_min_b[N] = INF
suffix_max_b[N] = -INF

for i in range(N - 1, -1, -1):
    idx = order[i]
    suffix_min_a[i] = min(suffix_min_a[i + 1], a[idx])
    suffix_max_a[i] = max(suffix_max_a[i + 1], a[idx])
    suffix_min_b[i] = min(suffix_min_b[i + 1], b[idx])
    suffix_max_b[i] = max(suffix_max_b[i + 1], b[idx])

ans = INF
for k in range(1, N):
    diam_left = max(max_a_prefix[k] - min_a_prefix[k], max_b_prefix[k] - min_b_prefix[k])
    diam_right = max(suffix_max_a[k] - suffix_min_a[k], suffix_max_b[k] - suffix_min_b[k])
    ans = min(ans, max(diam_left, diam_right))

print(ans)