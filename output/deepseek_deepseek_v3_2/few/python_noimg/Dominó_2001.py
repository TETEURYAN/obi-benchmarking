import sys

def solve():
    data = sys.stdin.read().split()
    idx = 0
    test_case = 1
    
    while idx < len(data):
        n = int(data[idx])
        idx += 1
        if n == 0:
            break
        
        degrees = [0] * 7
        adj = [[] for _ in range(7)]
        pecas = []
        
        for _ in range(n):
            x = int(data[idx])
            y = int(data[idx+1])
            idx += 2
            pecas.append((x, y))
            degrees[x] += 1
            degrees[y] += 1
            adj[x].append(y)
            adj[y].append(x)
        
        # Condição 1: verificar grau total par (exceto 0 ou 2 vértices com grau impar)
        odd_count = sum(1 for d in degrees if d % 2 == 1)
        if odd_count > 2:
            resultado = "nao"
        else:
            # Condição 2: conectividade - verificar se todas peças estão conectadas
            visited = [False] * 7
            start = -1
            for v in range(7):
                if degrees[v] > 0:
                    start = v
                    break
            
            if start != -1:
                stack = [start]
                visited[start] = True
                while stack:
                    u = stack.pop()
                    for v in adj[u]:
                        if not visited[v]:
                            visited[v] = True
                            stack.append(v)
            
            # Verificar se todos vértices com grau > 0 foram visitados
            connected = True
            for v in range(7):
                if degrees[v] > 0 and not visited[v]:
                    connected = False
                    break
            
            if connected:
                resultado = "sim"
            else:
                resultado = "nao"
        
        print(f"Teste {test_case}")
        print(resultado)
        print()
        test_case += 1

if __name__ == "__main__":
    solve()