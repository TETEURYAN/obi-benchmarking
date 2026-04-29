import sys

def main():
    data = sys.stdin.read().strip().split()
    i = 0
    teste = 1
    out = []

    while i < len(data):
        E = int(data[i])
        L = int(data[i + 1])
        i += 2

        if E == 0 and L == 0:
            break

        adj = [[] for _ in range(E + 1)]
        for _ in range(L):
            x = int(data[i])
            y = int(data[i + 1])
            i += 2
            adj[x].append(y)
            adj[y].append(x)

        visited = [False] * (E + 1)
        stack = [1]
        visited[1] = True
        count = 1

        while stack:
            u = stack.pop()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    count += 1
                    stack.append(v)

        estado = "normal" if count == E else "falha"

        out.append(f"Teste {teste}")
        out.append(estado)
        out.append("")
        teste += 1

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()