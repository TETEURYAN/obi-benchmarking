import sys
sys.setrecursionlimit(200000)

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    L = int(next(it))
    H = int(next(it))
    s = [int(next(it)) for _ in range(N)]
    m = [int(next(it)) for _ in range(N)]

    INF = 10**18
    # dp[k] = melhor soma de prefixo terminando na posição atual com exatamente k marcados
    dp = [-INF] * (H + 2)
    dp[0] = 0
    best = -INF

    prefix_sum = 0
    prefix_marked = 0
    # mantemos uma fila de prefixos para cada contagem de marcados
    queues = [[] for _ in range(H + 1)]
    for i in range(N):
        prefix_sum += s[i]
        prefix_marked += m[i]
        # atualiza dp para subsequências que começam em algum j <= i
        for k in range(H + 1):
            if k > prefix_marked:
                break
            # queremos o menor prefix_sum_old para (prefix_marked_old = prefix_marked - k)
            target = prefix_marked - k
            if target < 0:
                continue
            # mantemos a fila de prefix_sum_old para cada target em ordem crescente
            q = queues[target]
            while q and q[0][1] < i:  # remove prefixos muito antigos
                q.pop(0)
            if q:
                cand = prefix_sum - q[0][0]
                if cand > dp[k]:
                    dp[k] = cand
        # insere o prefixo atual na fila correspondente
        q = queues[prefix_marked]
        while q and q[-1][0] >= prefix_sum:
            q.pop()
        q.append((prefix_sum, i))
        # considera subsequências que terminam em i
        for k in range(L, H + 1):
            if dp[k] > best:
                best = dp[k]
        # também considera a subsequência vazia (soma 0) se L == 0
        if L == 0:
            best = max(best, 0)

    print(best)

if __name__ == "__main__":
    solve()