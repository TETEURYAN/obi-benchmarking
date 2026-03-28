import sys

def solve():
    # Leitura rápida de todos os dados de entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        # Leitura dos parâmetros iniciais
        X = int(next(iterator))
        Y = int(next(iterator))
        N = int(next(iterator))
        A = int(next(iterator))
    except StopIteration:
        return

    cities = []
    for _ in range(N):
        x = int(next(iterator))
        y = int(next(iterator))
        cities.append((x, y))

    # A distância entre cidades é dada por 100 * (|x1-x2| + |y1-y2|)
    # O carro consegue viajar se dist <= A
    # Logo, |x1-x2| + |y1-y2| <= A // 100
    limit = A // 100

    # Construção do grafo de adjacência
    # N <= 1000, logo O(N^2) é viável (aprox 10^6 operações)
    adj = [[] for _ in range(N)]
    
    for i in range(N):
        xi, yi = cities[i]
        for j in range(i + 1, N):
            xj, yj = cities[j]
            # Calcula distância de Manhattan
            dist_manhattan = abs(xi - xj) + abs(yi - yj)
            
            if dist_manhattan <= limit:
                adj[i].append(j)
                adj[j].append(i)

    # Contagem de componentes conectados usando DFS iterativo
    visited = [False] * N
    components = 0
    
    for i in range(N):
        if not visited[i]:
            components += 1
            stack = [i]
            visited[i] = True
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        stack.append(v)
    
    # O número de viagens de avião é o número de componentes - 1
    # Pois começamos em um componente e precisamos pular para os demais
    print(components - 1)

if __name__ == '__main__':
    solve()