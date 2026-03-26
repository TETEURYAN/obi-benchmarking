import sys
from collections import deque

# Otimização de leitura para competitivo
input_data = sys.stdin.read().split()

if not input_data:
    sys.exit(0)

iterator = iter(input_data)

try:
    # N: número de colunas, M: número de linhas
    N = int(next(iterator))
    M = int(next(iterator))
    P = int(next(iterator))
except StopIteration:
    sys.exit(0)

# Representação do mapa: grid[l][c] indica se há uma pedra na linha l, coluna c
# Dimensões: (M+1) x (N+1) para usar índices 1-based
grid = [[False] * (N + 1) for _ in range(M + 1)]

for _ in range(P):
    c = int(next(iterator))
    l = int(next(iterator))
    if 1 <= c <= N and 1 <= l <= M:
        grid[l][c] = True

try:
    Sc = int(next(iterator))
    Sl = int(next(iterator))
    Rc = int(next(iterator))
    Rl = int(next(iterator))
except StopIteration:
    sys.exit(0)

# BFS para encontrar caminho
# Matriz de visitados
visited = [[False] * (N + 1) for _ in range(M + 1)]
queue = deque()

# Verificação inicial de segurança (embora o problema garanta posições válidas)
if 1 <= Sc <= N and 1 <= Sl <= M:
    queue.append((Sc, Sl))
    visited[Sl][Sc] = True

# Movimentos: (delta_coluna, delta_linha)
# O problema permite saltos de 1, 2 ou 3 metros.
# Direções: Direita, Esquerda, Baixo, Cima
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

found = False

while queue:
    c, l = queue.popleft()

    if c == Rc and l == Rl:
        found = True
        break

    for dc, dl in directions:
        for dist in range(1, 4):
            nc = c + dc * dist
            nl = l + dl * dist

            # Verifica limites do lago
            if 1 <= nc <= N and 1 <= nl <= M:
                # Se for pedra e não visitado
                if grid[nl][nc] and not visited[nl][nc]:
                    visited[nl][nc] = True
                    queue.append((nc, nl))
            else:
                # Otimização: se saiu do lago, distâncias maiores na mesma direção também sairão
                break

print("S" if found else "N")