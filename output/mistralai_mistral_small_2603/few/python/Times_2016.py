
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    ptr = 0
    N = int(data[ptr])
    ptr += 1

    adj = [[] for _ in range(N + 1)]
    for i in range(1, N + 1):
        Mi = int(data[ptr])
        ptr += 1
        for _ in range(Mi):
            x = int(data[ptr])
            ptr += 1
            adj[i].append(x)

    team1 = []
    team2 = []
    color = [-1] * (N + 1)
    color[1] = 0
    team1.append(1)

    q = deque([1])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if color[v] == -1:
                color[v] = color[u] ^ 1
                if color[v] == 0:
                    team1.append(v)
                else:
                    team2.append(v)
                q.append(v)
            elif color[v] == color[u]:
                pass

    team1_sorted = sorted(team1)
    team2_sorted = sorted(team2)

    print(' '.join(map(str, team1_sorted)))
    print(' '.join(map(str, team2_sorted)))

if __name__ == "__main__":
    main()
