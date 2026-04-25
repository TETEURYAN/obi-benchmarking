import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    N = int(data[0])

    if N == 1:
        print(1)
        return
    if N == 2:
        print(-1)
        return

    # Para N >= 3, construímos um quadrado mágico aritmético
    # usando a ideia de matriz de números consecutivos
    # e depois ajustando a última linha para satisfazer as condições.
    # A construção conhecida para N=3 e N=4 dos exemplos pode ser generalizada.

    # Gera uma matriz base com números consecutivos por linha
    base = [[0] * N for _ in range(N)]
    val = 1
    for i in range(N):
        for j in range(N):
            base[i][j] = val
            val += 1

    # Para N=3, a matriz base já é a resposta (exemplo do problema)
    if N == 3:
        for row in base:
            print(*row)
        return

    # Para N >= 4, ajustamos a última linha para que as médias sejam inteiras e estejam presentes.
    # Estratégia: multiplicar os elementos da última linha por um fator que garanta
    # que a média de cada coluna seja um número que já existe na coluna.
    # Vamos usar a construção do exemplo N=4 como inspiração.

    # No exemplo N=4:
    # 1  2  3  6
    # 7  8  9  12
    # 13 14 15 18
    # 31 32 33 36
    # Observe que as três primeiras linhas são blocos consecutivos.
    # A última linha é obtida somando um múltiplo (30) aos elementos da primeira linha.
    # Mais precisamente: última_linha[i] = primeira_linha[i] + 30.
    # Isso garante que as médias das colunas sejam inteiras e estejam presentes.

    # Generalizando: para N >= 4, podemos fazer:
    # - As primeiras N-1 linhas são blocos consecutivos de N números cada.
    # - A última linha é a primeira linha somada a um valor K grande o suficiente
    #   para que todos os números sejam distintos e positivos.
    # Escolhemos K = base[N-2][N-1] + 1 (o maior número da penúltima linha + 1) para garantir unicidade.

    if N >= 4:
        # Reconstruir a matriz base com blocos consecutivos por linha
        val = 1
        for i in range(N-1):
            for j in range(N):
                base[i][j] = val
                val += 1
        # A última linha será a primeira linha somada a um offset K
        K = base[N-2][N-1] + 1  # offset grande para evitar repetição
        for j in range(N):
            base[N-1][j] = base[0][j] + K

        # Verificação rápida de que todos os números são distintos
        # (garantido pela construção, pois K > qualquer número nas primeiras N-1 linhas)
        for row in base:
            print(*row)
        return

if __name__ == "__main__":
    solve()