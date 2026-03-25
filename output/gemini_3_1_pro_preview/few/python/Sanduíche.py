import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

N = int(input_data[0])
M = int(input_data[1])

incompat = [0] * N
idx = 2
for _ in range(M):
    u = int(input_data[idx]) - 1
    v = int(input_data[idx+1]) - 1
    incompat[u] |= (1 << v)
    incompat[v] |= (1 << u)
    idx += 2

counts = {0: 1}
for i in range(N):
    new_counts = {}
    clear_mask = ~((1 << (i + 1)) - 1)
    incomp = incompat[i]
    bit_i = 1 << i
    for mask, cnt in counts.items():
        m1 = mask & clear_mask
        if m1 in new_counts:
            new_counts[m1] += cnt
        else:
            new_counts[m1] = cnt
            
        if not (mask & bit_i):
            m2 = (mask | incomp) & clear_mask
            if m2 in new_counts:
                new_counts[m2] += cnt
            else:
                new_counts[m2] = cnt
    counts = new_counts

print(sum(counts.values()) - 1)