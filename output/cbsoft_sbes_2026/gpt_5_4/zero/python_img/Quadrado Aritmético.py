import sys

def main():
    data = sys.stdin.readline().split()
    N = int(data[0])
    S = int(data[1])

    if N == 1:
        print(S)
        return

    # Construção:
    # a[i][j] = r[i] + c[j], com todos distintos.
    # Para qualquer permutação pi, soma_i a[i][pi(i)] =
    # sum(r) + sum(c), constante.
    #
    # Escolhemos:
    # r[i] = i * B
    # c[j] = j
    # e ajustamos a[0][0] somando delta para obter soma S.
    #
    # Para manter a propriedade de soma constante para qualquer escolha legal,
    # a matriz de ajustes deve ser da forma u[i] + v[j].
    # Basta somar delta em toda a linha 0 e subtrair delta em todas as outras linhas via colunas?
    # Mais simples: usar
    # a[i][j] = i*B + j + x[i] + y[j]
    # então qualquer escolha legal soma sum(i*B+x[i]) + sum(j+y[j]).
    #
    # Tomamos y[j]=j e x[i]=i*B, e ajustamos x[0] por delta.
    # Assim a[i][j] = i*B + j, exceto linha 0 recebe +delta em todas as colunas.
    # Todos os valores continuam distintos se B > N + |delta|.
    #
    # Soma de qualquer escolha legal:
    # base = B * N*(N-1)/2 + N*(N-1)/2
    # total = base + delta
    # logo delta = S - base.

    B = 10**6
    base = (N * (N - 1) // 2) * (B + 1)
    delta = S - base

    # Garantia de distinção:
    # linha 0: j + delta
    # linha i>0: i*B + j
    # entre linhas i1!=i2>0 já são distintas pois B>N.
    # linha 0 não colide com outras se |delta| + (N-1) < B - (N-1), o que vale
    # para nossos limites: |delta| <= ~5e11 seria problema, então precisamos
    # escolher construção melhor para respeitar limites de célula e distinção.
    #
    # Vamos usar construção mais controlada:
    # a[i][j] = p[i] + q[j]
    # com p[i] = i*M
    # q[j] = j
    # e depois somamos t a todas as células, e distribuímos resto em q[0].
    # Soma legal = sum(p)+sum(q)+N*t.
    #
    # Queremos atingir qualquer S sem explodir valores:
    # Escolha M = 2000.
    # Então base pequeno.
    # Ajuste por t = floor((S-base)/N), resto em q[0].
    # Soma vira base + N*t + resto.
    # Distinção preservada se M > N + |resto|, com resto < N.
    # Como N<=1000, M=2005 serve.

    M = 2005
    sum_p = M * N * (N - 1) // 2
    sum_q = N * (N - 1) // 2
    base = sum_p + sum_q

    diff = S - base
    t = diff // N
    r = diff - t * N  # 0 <= r < N

    # Matriz: a[i][j] = i*M + j + t, e adiciona r em q[0], isto é, coluna 0.
    # Soma legal = sum_p + (sum_q + r) + N*t = S.
    # Distinção:
    # dentro da mesma linha, colunas distintas diferem por j.
    # entre linhas diferentes, diferença principal é múltiplo de M, com ajuste de coluna <= N.
    # Como M > 2N, não há colisão mesmo com coluna 0 tendo +r (<N).

    out = []
    for i in range(N):
        row = []
        base_i = i * M + t
        for j in range(N):
            val = base_i + j + (r if j == 0 else 0)
            row.append(str(val))
        out.append(" ".join(row))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
