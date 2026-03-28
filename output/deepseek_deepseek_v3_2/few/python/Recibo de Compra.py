import sys
sys.setrecursionlimit(200000)

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    R = int(data[0])
    K = int(data[1])

    # dp[i][j][l] = número de maneiras de somar i usando j números distintos, sendo o maior número usado <= l
    # Usamos rotação de dimensão para economizar memória
    max_num = R
    dp_prev = [[0] * (max_num + 2) for _ in range(K + 1)]
    dp_prev[0][0] = 1  # base: 0 números somando 0

    for num in range(1, max_num + 1):
        dp_curr = [row[:] for row in dp_prev]
        for sum_val in range(num, R + 1):
            for cnt in range(1, K + 1):
                dp_curr[cnt][sum_val] += dp_prev[cnt - 1][sum_val - num]
        dp_prev = dp_curr

    # Resposta: número de maneiras de somar R com K números distintos, com maior número <= R
    print(dp_prev[K][R])

if __name__ == "__main__":
    main()