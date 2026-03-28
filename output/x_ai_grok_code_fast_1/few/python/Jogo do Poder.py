import sys
import heapq

data = sys.stdin.read().split()
index = 0
N = int(data[index])
index += 1
M = int(data[index])
index += 1

P = []
for i in range(N):
    row = []
    for j in range(M):
        row.append(int(data[index]))
        index += 1
    P.append(row)

power_max = [[P[i][j] for j in range(M)] for i in range(N)]

pq = []
for i in range(N):
    for j in range(M):
        heapq.heappush(pq, (-P[i][j], i, j))

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while pq:
    neg_p, i, j = heapq.heappop(pq)
    p = -neg_p
    if p < power_max[i][j]:
        continue
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < M:
            if p >= P[ni][nj]:
                new_p = p + P[ni][nj]
                if new_p > power_max[ni][nj]:
                    power_max[ni][nj] = new_p
                    heapq.heappush(pq, (-new_p, ni, nj))

for i in range(N):
    print(' '.join(map(str, power_max[i])))