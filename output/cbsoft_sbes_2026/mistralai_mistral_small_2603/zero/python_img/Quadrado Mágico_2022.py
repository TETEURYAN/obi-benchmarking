
def main():
    N = int(input())
    quadrado = []
    for _ in range(N):
        linha = list(map(int, input().split()))
        quadrado.append(linha)

    soma_magica = None
    pos_zero = (0, 0)

    for i in range(N):
        for j in range(N):
            if quadrado[i][j] == 0:
                pos_zero = (i, j)

    i, j = pos_zero

    if i == 0 and j == 0:
        soma_linha = sum(quadrado[1])
        soma_coluna = sum(quadrado[i][k] for k in range(N) if k != j)
        soma_diagonal = sum(quadrado[k][k] for k in range(N) if k != i)
        if soma_linha == soma_coluna:
            soma_magica = soma_linha
        else:
            soma_magica = soma_diagonal
    elif i == 0:
        soma_linha = sum(quadrado[1])
        soma_coluna = sum(quadrado[k][j] for k in range(N) if k != i)
        soma_magica = soma_linha
    elif j == 0:
        soma_linha = sum(quadrado[i])
        soma_coluna = sum(quadrado[k][1] for k in range(N) if k != i)
        soma_magica = soma_linha
    else:
        soma_linha = sum(quadrado[i])
        soma_coluna = sum(quadrado[k][j] for k in range(N) if k != i)
        if i == j:
            soma_diagonal = sum(quadrado[k][k] for k in range(N) if k != i)
            if soma_linha == soma_coluna:
                soma_magica = soma_linha
            else:
                soma_magica = soma_diagonal
        else:
            soma_magica = soma_linha

    valor = soma_magica - (soma_linha - 0)
    print(valor)
    print(i + 1)
    print(j + 1)

if __name__ == "__main__":
    main()
