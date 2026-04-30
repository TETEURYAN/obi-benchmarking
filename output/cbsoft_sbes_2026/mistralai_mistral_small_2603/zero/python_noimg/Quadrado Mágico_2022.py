
def main():
    N = int(input())
    quadrado = []
    for _ in range(N):
        linha = list(map(int, input().split()))
        quadrado.append(linha)

    soma_magica = None
    for i in range(N):
        soma_linha = sum(quadrado[i])
        if 0 not in quadrado[i]:
            soma_magica = soma_linha
            break

    if soma_magica is None:
        for j in range(N):
            soma_coluna = sum(quadrado[i][j] for i in range(N))
            if 0 not in [quadrado[i][j] for i in range(N)]:
                soma_magica = soma_coluna
                break

    if soma_magica is None:
        soma_diag1 = sum(quadrado[i][i] for i in range(N))
        if 0 not in [quadrado[i][i] for i in range(N)]:
            soma_magica = soma_diag1
        else:
            soma_diag2 = sum(quadrado[i][N-1-i] for i in range(N))
            soma_magica = soma_diag2

    for i in range(N):
        for j in range(N):
            if quadrado[i][j] == 0:
                quadrado[i][j] = soma_magica - sum(quadrado[i])
                print(quadrado[i][j])
                print(i + 1)
                print(j + 1)
                return

if __name__ == "__main__":
    main()
