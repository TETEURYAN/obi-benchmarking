import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    adj = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        mi = int(next(it))
        for _ in range(mi):
            x = int(next(it))
            adj[i].append(x)
    cor = [-1] * (n + 1)
    q = deque()
    cor[1] = 0
    q.append(1)
    while q:
        u = q.popleft()
        for v in adj[u]:
            if cor[v] == -1:
                cor[v] = 1 - cor[u]
                q.append(v)
    for i in range(1, n + 1):
        if cor[i] == -1:
            cor[i] = 0
            q.append(i)
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if cor[v] == -1:
                        cor[v] = 1 - cor[u]
                        q.append(v)
    time1 = [i for i in range(1, n + 1) if cor[i] == 0]
    time2 = [i for i in range(1, n + 1) if cor[i] == 1]
    print(' '.join(map(str, time1)))
    print(' '.join(map(str, time2)))

if __name__ == '__main__':
    main()