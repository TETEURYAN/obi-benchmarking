import sys

sys.setrecursionlimit(200000)

input_data = sys.stdin.read().split()

idx = 0

N = int(input_data[idx])

idx += 1

M = int(input_data[idx])

idx += 1

plans = []

for _ in range(M):

    U = int(input_data[idx])

    L = int(input_data[idx + 1])

    R = int(input_data[idx + 2])

    plans.append((U, L, R))

    idx += 3

def has_cycle(mid):

    adj = [[] for _ in range(N + 1)]

    for i in range(mid):

        U, L, R = plans[i]

        adj[U].append((L, R))

    for u in range(1, N + 1):

        if not adj[u]:

            continue

        adj[u].sort()

        merged = []

        if adj[u]:

            current_L, current_R = adj[u][0]

            for L, R in adj[u][1:]:

                if L <= current_R + 1:

                    current_R = max(current_R, R)

                else:

                    merged.append((current_L, current_R))

                    current_L, current_R = L, R

            merged.append((current_L, current_R))

        adj[u] = merged

    color = [0] * (N + 1)

    def DFS(u):

        if color[u] == 1:

            return True

        if color[u] == 2:

            return False

        color[u] = 1

        for L, R in adj[u]:

            for v in range(L, R + 1):

                if DFS(v):

                    return True

        color[u] = 2

        return False

    for start in range(1, N + 1):

        if color[start] == 0:

            if DFS(start):

                return True

    return False

left = 1

right = M

ans = -1

while left <= right:

    mid = (left + right) // 2

    if has_cycle(mid):

        ans = mid

        right = mid - 1

    else:

        left = mid + 1

print(ans)