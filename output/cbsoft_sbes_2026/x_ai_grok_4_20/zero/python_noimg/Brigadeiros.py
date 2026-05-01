
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
K = int(data[1])
T = int(data[2])
P = [int(x) for x in data[3:3+N]]
G = [int(x) for x in data[3+N:3+2*N]]

positions = []
for i in range(N):
    if G[i] == 1:
        positions.append(i)

prefix = [0] * (N + 1)
for i in range(1, N + 1):
    prefix[i] = prefix[i - 1] + P[i - 1]

def range_sum(l, r):
    return prefix[r + 1] - prefix[l]

ans = 0
for start in range(N - K + 1):
    target = list(range(start, start + K))
    cost = 0
    for i in range(K):
        cost += abs(positions[i] - target[i])
    if cost <= T:
        current = range_sum(start, start + K - 1)
        if current > ans:
            ans = current

if T == 0 or K == 1:
    current = 0
    for i in range(N):
        if G[i] == 1:
            current += P[i]
    print(current)
    sys.exit(0)

max_pos = N - 1
for leftmost in range(N):
    for rightmost in range(leftmost + K - 1, N):
        if rightmost - leftmost + 1 < K:
            continue
        needed = K
        j = 0
        selected = []
        for i in range(leftmost, rightmost + 1):
            while j < K and positions[j] < i:
                j += 1
            if j < K and positions[j] == i:
                selected.append(i)
                needed -= 1
                j += 1
            if needed == 0:
                break
        if len(selected) < K:
            continue
        L = leftmost
        R = rightmost
        min_cost = 0
        for i in range(K):
            min_cost += abs(selected[i] - (L + i))
        if min_cost > T:
            continue
        current = range_sum(L, R)
        if current > ans:
            ans = current
        for M in range(L + 1, R - K + 2):
            new_cost = min_cost
            new_cost -= abs(selected[0] - L)
            for i in range(1, K):
                new_cost += abs(selected[i] - (L + i)) - abs(selected[i - 1] - (L + i))
            new_cost += abs(selected[K - 1] - (L + K))
            min_cost = new_cost
            L += 1
            if min_cost <= T:
                if current > ans:
                    ans = current
print(ans)
