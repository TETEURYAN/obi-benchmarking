
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    idx = 0
    N = int(data[idx])
    idx += 1
    F = [0] * (N + 1)
    for i in range(1, N + 1):
        F[i] = int(data[idx])
        idx += 1

    Q = int(data[idx])
    idx += 1
    queries = []
    for _ in range(Q):
        A = int(data[idx])
        B = int(data[idx + 1])
        queries.append((A, B))
        idx += 2

    in_cycle = [False] * (N + 1)
    visited = [False] * (N + 1)
    cycle_nodes = []

    for i in range(1, N + 1):
        if not visited[i]:
            path = []
            current = i
            while True:
                if visited[current]:
                    if current in path:
                        cycle_start = current
                        cycle_idx = path.index(cycle_start)
                        cycle_nodes.extend(path[cycle_idx:])
                        for node in path[cycle_idx:]:
                            in_cycle[node] = True
                    break
                visited[current] = True
                path.append(current)
                current = F[current]

    cycle_size = len(cycle_nodes)
    pos_in_cycle = [0] * (N + 1)
    for i in range(cycle_size):
        node = cycle_nodes[i]
        pos_in_cycle[node] = i

    dist_to_cycle = [0] * (N + 1)
    for node in range(1, N + 1):
        if in_cycle[node]:
            dist_to_cycle[node] = 0
        else:
            current = node
            steps = 0
            while not in_cycle[current]:
                current = F[current]
                steps += 1
            dist_to_cycle[node] = steps

    cycle_dist = [[0] * cycle_size for _ in range(cycle_size)]
    for i in range(cycle_size):
        for j in range(cycle_size):
            diff = (j - i) % cycle_size
            cycle_dist[i][j] = min(diff, cycle_size - diff)

    out = []
    for A, B in queries:
        if A == B:
            out.append("0")
            continue

        dist_a = dist_to_cycle[A]
        dist_b = dist_to_cycle[B]

        if in_cycle[A] and in_cycle[B]:
            d = cycle_dist[pos_in_cycle[A]][pos_in_cycle[B]]
            out.append(str(d))
        elif in_cycle[A]:
            d = dist_b + cycle_dist[pos_in_cycle[A]][pos_in_cycle[F[B]]]
            out.append(str(d))
        elif in_cycle[B]:
            d = dist_a + cycle_dist[pos_in_cycle[F[A]]][pos_in_cycle[B]]
            out.append(str(d))
        else:
            d1 = dist_a + dist_b + cycle_dist[pos_in_cycle[F[A]]][pos_in_cycle[F[B]]]
            d2 = dist_a + cycle_dist[pos_in_cycle[F[A]]][pos_in_cycle[B]] + dist_b
            d3 = cycle_dist[pos_in_cycle[A]][pos_in_cycle[F[B]]] + dist_a + dist_b
            d4 = cycle_dist[pos_in_cycle[A]][pos_in_cycle[B]]
            out.append(str(min(d1, d2, d3, d4)))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
