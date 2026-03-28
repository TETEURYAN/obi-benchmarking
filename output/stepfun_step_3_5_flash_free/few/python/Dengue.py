import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    teste = 1
    while idx < len(data):
        n = int(data[idx]); idx += 1
        if n == 0:
            break
        adj = [[] for _ in range(n+1)]
        grau = [0]*(n+1)
        for _ in range(n-1):
            u = int(data[idx]); v = int(data[idx+1]); idx += 2
            adj[u].append(v)
            adj[v].append(u)
            grau[u] += 1
            grau[v] += 1
        if n == 1:
            centro = 1
        else:
            ativo = [True]*(n+1)
            fila = deque()
            for i in range(1, n+1):
                if grau[i] == 1:
                    fila.append(i)
            n_restantes = n
            while n_restantes > 2:
                nova_fila = deque()
                for _ in range(len(fila)):
                    u = fila.popleft()
                    if not ativo[u]:
                        continue
                    ativo[u] = False
                    n_restantes -= 1
                    for v in adj[u]:
                        if ativo[v]:
                            grau[v] -= 1
                            if grau[v] == 1:
                                nova_fila.append(v)
                fila = nova_fila
            centros = [i for i in range(1, n+1) if ativo[i]]
            centro = min(centros)
        print(f"Teste {teste}")
        print(centro)
        print()
        teste += 1

if __name__ == "__main__":
    main()