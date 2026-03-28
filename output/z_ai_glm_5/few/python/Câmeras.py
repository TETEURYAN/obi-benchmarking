import sys
from collections import deque

def solve():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        N = int(next(iterator))
        M = int(next(iterator))
        K = int(next(iterator))
    except StopIteration:
        return

    # Matriz de observação: observed[coluna][linha]
    # Dimensões: (N+1) x (M+1) para índices de 1 a N e 1 a M
    observed = [[False] * (M + 1) for _ in range(N + 1)]

    # Processamento das câmeras
    for _ in range(K):
        try:
            Ci = int(next(iterator))
            Li = int(next(iterator))
            Di = next(iterator)
        except StopIteration:
            break
        
        if Di == 'N':
            # Norte: mesma coluna, linhas 1 até Li
            for l in range(1, Li + 1):
                observed[Ci][l] = True
        elif Di == 'S':
            # Sul: mesma coluna, linhas Li até M
            for l in range(Li, M + 1):
                observed[Ci][l] = True
        elif Di == 'O':
            # Oeste: mesma linha, colunas 1 até Ci
            for c in range(1, Ci + 1):
                observed[c][Li] = True
        elif Di == 'L':
            # Leste: mesma linha, colunas Ci até N
            for c in range(Ci, N + 1):
                observed[c][Li] = True

    # Verificação inicial: entrada ou saída bloqueada
    if observed[1][1] or observed[N][M]:
        print("N")
        return

    # BFS para encontrar caminho
    # Fila armazena tuplas (coluna, linha)
    queue = deque([(1, 1)])
    visited = [[False] * (M + 1) for _ in range(N + 1)]
    visited[1][1] = True

    # Movimentos: Norte, Sul, Leste, Oeste
    # (dc, dl)
    moves = [(0, -1), (0, 1), (1, 0), (-1, 0)]

    while queue:
        c, l = queue.popleft()

        if c == N and l == M:
            print("S")
            return

        for dc, dl in moves:
            nc, nl = c + dc, l + dl
            
            # Verifica limites do grid
            if 1 <= nc <= N and 1 <= nl <= M:
                # Verifica se não foi observado e não visitado
                if not observed[nc][nl] and not visited[nc][nl]:
                    visited[nc][nl] = True
                    queue.append((nc, nl))

    print("N")

if __name__ == '__main__':
    solve()