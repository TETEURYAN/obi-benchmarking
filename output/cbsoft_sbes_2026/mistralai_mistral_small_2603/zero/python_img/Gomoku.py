
def verifica_vencedor(tabuleiro):
    n = 15
    for i in range(n):
        for j in range(n):
            if tabuleiro[i][j] == 0:
                continue
            cor = tabuleiro[i][j]
            # Verifica horizontal
            if j + 4 < n:
                if all(tabuleiro[i][j+k] == cor for k in range(5)):
                    return cor
            # Verifica vertical
            if i + 4 < n:
                if all(tabuleiro[i+k][j] == cor for k in range(5)):
                    return cor
            # Verifica diagonal principal
            if i + 4 < n and j + 4 < n:
                if all(tabuleiro[i+k][j+k] == cor for k in range(5)):
                    return cor
            # Verifica diagonal secundária
            if i + 4 < n and j - 4 >= 0:
                if all(tabuleiro[i+k][j-k] == cor for k in range(5)):
                    return cor
    return 0

def main():
    tabuleiro = []
    for _ in range(15):
        linha = list(map(int, input().split()))
        tabuleiro.append(linha)
    vencedor = verifica_vencedor(tabuleiro)
    print(vencedor)

if __name__ == "__main__":
    main()
