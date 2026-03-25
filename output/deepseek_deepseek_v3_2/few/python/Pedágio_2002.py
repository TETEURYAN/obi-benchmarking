import sys

def main():
    data = sys.stdin.read().strip().split()
    idx = 0
    test_num = 1
    output_lines = []

    while True:
        C = int(data[idx]); idx += 1
        E = int(data[idx]); idx += 1
        L = int(data[idx]); idx += 1
        P = int(data[idx]); idx += 1

        if C == 0 and E == 0 and L == 0 and P == 0:
            break

        adj = [[] for _ in range(C + 1)]
        for _ in range(E):
            X = int(data[idx]); idx += 1
            Y = int(data[idx]); idx += 1
            adj[X].append(Y)
            adj[Y].append(X)

        dist = [-1] * (C + 1)
        dist[L] = 0
        queue = [L]
        front = 0

        while front < len(queue):
            u = queue[front]
            front += 1
            if dist[u] == P:
                continue
            for v in adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    queue.append(v)

        reachable = []
        for city in range(1, C + 1):
            if city != L and 0 < dist[city] <= P:
                reachable.append(city)

        output_lines.append(f"Teste {test_num}")
        output_lines.append(" ".join(map(str, reachable)))
        output_lines.append("")
        test_num += 1

    sys.stdout.write("\n".join(output_lines))

if __name__ == "__main__":
    main()