
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    idx = 0
    E = int(data[idx])
    I = int(data[idx+1])
    V = int(data[idx+2])
    idx += 3

    adj = [[] for _ in range(E + 1)]
    in_degree = [0] * (E + 1)

    for _ in range(I):
        A = int(data[idx])
        B = int(data[idx+1])
        adj[A].append(B)
        in_degree[B] += 1
        idx += 2

    initial_events = list(map(int, data[idx:idx+V]))
    idx += V

    queue = deque()
    for event in initial_events:
        queue.append(event)

    result = set(initial_events)

    while queue:
        u = queue.popleft()
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                result.add(v)
                queue.append(v)

    print(' '.join(map(str, sorted(result))))

if __name__ == "__main__":
    main()
