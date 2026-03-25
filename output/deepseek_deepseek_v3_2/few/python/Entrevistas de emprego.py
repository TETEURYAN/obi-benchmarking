
import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return

    idx = 0
    N = int(data[idx])
    idx += 1

    adj = [[0] * N for _ in range(N)]
    for i in range(N):
        row = data[idx]
        idx += 1
        for j in range(N):
            adj[i][j] = int(row[j])

    color = [-1] * N
    stack = []
    for i in range(N):
        if color[i] != -1:
            continue
        color[i] = 0
        stack.append(i)
        while stack:
            u = stack.pop()
            for v in range(N):
                if adj[u][v] == 1:
                    if color[v] == -1:
                        color[v] = color[u] ^ 1
                        stack.append(v)
                    elif color[v] == color[u]:
                        # This should not happen according to problem constraints.
                        pass

    E = int(data[idx])
    idx += 1
    output_lines = []
    for _ in range(E):
        Ki = int(data[idx])
        idx += 1
        candidates = []
        for j in range(Ki):
            c = int(data[idx]) - 1  # convert to 0‑based
            idx += 1
            candidates.append(c)

        same_group = False
        for a in candidates:
            for b in candidates:
                if a != b and adj[a][b] == 1:
                    same_group = True
                    break
            if same_group:
                break

        output_lines.append("S" if same_group else "N")

    sys.stdout.write("\n".join(output_lines))

if __name__ == "__main__":
    main()
