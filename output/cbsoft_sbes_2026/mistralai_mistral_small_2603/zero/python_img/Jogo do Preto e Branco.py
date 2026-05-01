
def main():
    import sys
    data = sys.stdin.read().split()
    idx = 0
    L = int(data[idx])
    idx += 1
    C = int(data[idx])
    idx += 1
    P = int(data[idx])
    idx += 1

    pretas = set()
    for _ in range(P):
        x = int(data[idx])
        idx += 1
        y = int(data[idx])
        idx += 1
        pretas.add((x, y))

    tabuleiro = [[0] * (C + 1) for _ in range(L + 1)]
    for (x, y) in pretas:
        tabuleiro[x][y] = 1

    brancas = set()
    direcoes = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for i in range(1, L + 1):
        for j in range(1, C + 1):
            if tabuleiro[i][j] == 0:
                for dx, dy in direcoes:
                    ni, nj = i + dx, j + dy
                    if 1 <= ni <= L and 1 <= nj <= C and tabuleiro[ni][nj] == 1:
                        brancas.add((i, j))
                        break

    while True:
        adicionadas = set()
        for (i, j) in brancas:
            for dx, dy in direcoes:
                ni, nj = i + dx, j + dy
                if 1 <= ni <= L and 1 <= nj <= C and tabuleiro[ni][nj] == 0 and (ni, nj) not in brancas:
                    tabuleiro[ni][nj] = 2
                    adicionadas.add((ni, nj))
        if not adicionadas:
            break
        brancas.update(adicionadas)

    print(len(brancas))

if __name__ == "__main__":
    main()
