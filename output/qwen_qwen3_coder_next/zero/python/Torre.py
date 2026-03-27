
n = int(input())
tabuleiro = []
for _ in range(n):
    linha = list(map(int, input().split()))
    tabuleiro.append(linha)

# Pré-computar somas das linhas e colunas
soma_linhas = [sum(linha) for linha in tabuleiro]
soma_colunas = [sum(tabuleiro[i][j] for i in range(n)) for j in range(n)]

maximo = 0
for i in range(n):
    for j in range(n):
        # Peso = (soma da linha i) + (soma da coluna j) - 2 * tabuleiro[i][j]
        # Subtraímos 2 * tabuleiro[i][j] porque ele é contado tanto na linha quanto na coluna,
        # mas não deve ser contado no peso
        peso = soma_linhas[i] + soma_colunas[j] - 2 * tabuleiro[i][j]
        if peso > maximo:
            maximo = peso

print(maximo)
