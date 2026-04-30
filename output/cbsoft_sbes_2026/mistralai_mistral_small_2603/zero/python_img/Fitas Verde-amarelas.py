
import sys

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        print(0)
        return
    n, m = map(int, data[0].split())
    grid = []
    for i in range(1, 1 + n):
        grid.append(data[i].strip())

    # Direções: cima, baixo, esquerda, direita
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Vamos processar o grid para encontrar regiões de terra conectadas
    visited = [[False for _ in range(m)] for _ in range(n)]
    total_tapes = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] == '#' and not visited[i][j]:
                # BFS para encontrar a região de terra conectada
                queue = [(i, j)]
                visited[i][j] = True
                region = []
                while queue:
                    x, y = queue.pop(0)
                    region.append((x, y))
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < m:
                            if grid[nx][ny] == '#' and not visited[nx][ny]:
                                visited[nx][ny] = True
                                queue.append((nx, ny))

                # Agora, precisamos cobrir essa região com fitas verdes (horizontais) e amarelas (verticais)
                # A estratégia é cobrir o máximo possível com fitas verdes (mais eficiente em termos de número de fitas)
                # e o restante com fitas amarelas, garantindo que não haja adjacência entre fitas de cores diferentes.

                # Primeiro, tentamos cobrir o máximo possível com fitas verdes (horizontais)
                # Para isso, agrupamos células na mesma linha que são adjacentes horizontalmente
                rows = {}
                for x, y in region:
                    if x not in rows:
                        rows[x] = []
                    rows[x].append(y)

                green_tapes = 0
                for x in rows:
                    ys = sorted(rows[x])
                    i_ys = 0
                    while i_ys < len(ys):
                        start = ys[i_ys]
                        end = start
                        while i_ys + 1 < len(ys) and ys[i_ys + 1] == end + 1:
                            end += 1
                            i_ys += 1
                        green_tapes += 1
                        i_ys += 1

                # Agora, precisamos cobrir as células restantes com fitas amarelas (verticais)
                # Mas precisamos garantir que nenhuma célula coberta por fita verde seja vizinha de uma coberta por fita amarela
                # Para isso, marcamos as células que estão cobertas por fitas verdes e suas vizinhas como não podendo ser cobertas por fitas amarelas

                # Criamos uma matriz para marcar células cobertas por fitas verdes
                covered_by_green = [[False for _ in range(m)] for _ in range(n)]
                for x in rows:
                    ys = sorted(rows[x])
                    i_ys = 0
                    while i_ys < len(ys):
                        start = ys[i_ys]
                        end = start
                        while i_ys + 1 < len(ys) and ys[i_ys + 1] == end + 1:
                            end += 1
                            i_ys += 1
                        for y in range(start, end + 1):
                            covered_by_green[x][y] = True
                        i_ys += 1

                # Agora, marcamos as células vizinhas às cobertas por fitas verdes como não podendo ser cobertas por fitas amarelas
                forbidden_for_yellow = [[False for _ in range(m)] for _ in range(n)]
                for x in range(n):
                    for y in range(m):
                        if covered_by_green[x][y]:
                            for dx, dy in directions:
                                nx, ny = x + dx, y + dy
                                if 0 <= nx < n and 0 <= ny < m:
                                    forbidden_for_yellow[nx][ny] = True

                # Agora, contamos as células restantes que precisam ser cobertas por fitas amarelas
                yellow_cells = 0
                for x, y in region:
                    if not covered_by_green[x][y] and not forbidden_for_yellow[x][y]:
                        yellow_cells += 1

                # Cada fita amarela cobre uma coluna contígua de células não cobertas por fitas verdes e não adjacentes a fitas verdes
                # Para minimizar o número de fitas amarelas, agrupamos células na mesma coluna que são adjacentes verticalmente
                cols = {}
                for x, y in region:
                    if not covered_by_green[x][y] and not forbidden_for_yellow[x][y]:
                        if y not in cols:
                            cols[y] = []
                        cols[y].append(x)

                yellow_tapes = 0
                for y in cols:
                    xs = sorted(cols[y])
                    i_xs = 0
                    while i_xs < len(xs):
                        start = xs[i_xs]
                        end = start
                        while i_xs + 1 < len(xs) and xs[i_xs + 1] == end + 1:
                            end += 1
                            i_xs += 1
                        yellow_tapes += 1
                        i_xs += 1

                total_tapes += green_tapes + yellow_tapes

    print(total_tapes)

if __name__ == "__main__":
    main()
