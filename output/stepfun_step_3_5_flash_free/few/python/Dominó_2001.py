import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    test_num = 1
    while idx < len(data):
        n = int(data[idx]); idx += 1
        if n == 0:
            break
        grau = [0] * 7
        adj = [[] for _ in range(7)]
        for _ in range(n):
            x = int(data[idx]); y = int(data[idx+1]); idx += 2
            grau[x] += 1
            grau[y] += 1
            if x != y:
                adj[x].append(y)
                adj[y].append(x)
        impares = sum(1 for g in grau if g % 2 == 1)
        start = -1
        for v in range(7):
            if grau[v] > 0:
                start = v
                break
        if start == -1:
            conexo = True
        else:
            visited = [False] * 7
            queue = deque([start])
            visited[start] = True
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        queue.append(v)
            conexo = True
            for v in range(7):
                if grau[v] > 0 and not visited[v]:
                    conexo = False
                    break
        if conexo and (impares == 0 or impares == 2):
            resultado = "sim"
        else:
            resultado = "nao"
        print(f"Teste {test_num}")
        print(resultado)
        print()
        test_num += 1

if __name__ == "__main__":
    main()