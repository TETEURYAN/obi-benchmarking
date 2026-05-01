import sys

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    grid = [input().strip() for _ in range(N)]

    # id of horizontal segments
    hid = [[-1] * M for _ in range(N)]
    hcnt = 0
    for i in range(N):
        j = 0
        row = grid[i]
        while j < M:
            if row[j] == '#':
                hcnt += 1
                while j < M and row[j] == '#':
                    hid[i][j] = hcnt - 1
                    j += 1
            else:
                j += 1

    # id of vertical segments
    vid = [[-1] * M for _ in range(N)]
    vcnt = 0
    for j in range(M):
        i = 0
        while i < N:
            if grid[i][j] == '#':
                vcnt += 1
                while i < N and grid[i][j] == '#':
                    vid[i][j] = vcnt - 1
                    i += 1
            else:
                i += 1

    # Build bipartite graph:
    # horizontal segment h conflicts with vertical segment v
    # if there exists adjacent land cells, one in h and one in v.
    adj = [[] for _ in range(hcnt)]

    for i in range(N):
        for j in range(M):
            if grid[i][j] != '#':
                continue
            h = hid[i][j]
            v = vid[i][j]

            if j + 1 < M and grid[i][j + 1] == '#':
                v2 = vid[i][j + 1]
                if v != v2:
                    adj[h].append(v2)
                h2 = hid[i][j + 1]
                if h != h2:
                    adj[h2].append(v)

            if i + 1 < N and grid[i + 1][j] == '#':
                h2 = hid[i + 1][j]
                if h != h2:
                    adj[h].append(vid[i + 1][j])
                v2 = vid[i + 1][j]
                if v != v2:
                    adj[h2].append(v)

    # Hopcroft-Karp for maximum matching
    from collections import deque

    pair_u = [-1] * hcnt
    pair_v = [-1] * vcnt
    dist = [-1] * hcnt

    def bfs():
        q = deque()
        for u in range(hcnt):
            if pair_u[u] == -1:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = -1
        found = False
        while q:
            u = q.popleft()
            for v in adj[u]:
                pu = pair_v[v]
                if pu == -1:
                    found = True
                elif dist[pu] == -1:
                    dist[pu] = dist[u] + 1
                    q.append(pu)
        return found

    def dfs(u):
        for v in adj[u]:
            pu = pair_v[v]
            if pu == -1 or (dist[pu] == dist[u] + 1 and dfs(pu)):
                pair_u[u] = v
                pair_v[v] = u
                return True
        dist[u] = -1
        return False

    matching = 0
    while bfs():
        for u in range(hcnt):
            if pair_u[u] == -1 and dfs(u):
                matching += 1

    # Minimum tapes = minimum weighted vertex cover in conflict graph
    # Since every horizontal/vertical segment costs 1, answer is:
    # total segments - maximum matching
    print(hcnt + vcnt - matching)

if __name__ == "__main__":
    main()
