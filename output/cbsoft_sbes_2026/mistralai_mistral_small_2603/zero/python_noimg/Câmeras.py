
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    ptr = 0
    N = int(data[ptr]); ptr += 1
    M = int(data[ptr]); ptr += 1
    K = int(data[ptr]); ptr += 1

    cameras = []
    for _ in range(K):
        Ci = int(data[ptr]); ptr += 1
        Li = int(data[ptr]); ptr += 1
        Di = data[ptr]; ptr += 1
        cameras.append((Ci, Li, Di))

    # Direções: N, S, L, O
    # Vamos marcar as células que são observadas por câmeras
    observed = [[False] * (M + 1) for _ in range(N + 1)]

    for Ci, Li, Di in cameras:
        if Di == 'N':
            for l in range(Li, M + 1):
                observed[Ci][l] = True
        elif Di == 'S':
            for l in range(1, Li + 1):
                observed[Ci][l] = True
        elif Di == 'L':
            for c in range(Ci, N + 1):
                observed[c][Li] = True
        elif Di == 'O':
            for c in range(1, Ci + 1):
                observed[c][Li] = True

    # Verificar se a entrada ou saída estão observadas
    if observed[1][1] or observed[N][M]:
        print('N')
        return

    # BFS para verificar se há caminho da entrada (1,1) para saída (N,M)
    visited = [[False] * (M + 1) for _ in range(N + 1)]
    queue = deque()
    queue.append((1, 1))
    visited[1][1] = True

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        c, l = queue.popleft()
        if c == N and l == M:
            print('S')
            return

        for dc, dl in directions:
            nc, nl = c + dc, l + dl
            if 1 <= nc <= N and 1 <= nl <= M:
                if not observed[nc][nl] and not visited[nc][nl]:
                    visited[nc][nl] = True
                    queue.append((nc, nl))

    print('N')

if __name__ == '__main__':
    main()
