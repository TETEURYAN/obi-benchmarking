import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    A = [int(next(it)) for _ in range(N)]
    
    opcoes = []
    for a in A:
        o1 = a
        o2 = M - a
        if o1 == o2:
            opcoes.append([o1])
        else:
            opcoes.append([o1, o2])
    
    INF = 10**18
    dp_prev = [x for x in opcoes[0]]
    
    for i in range(1, N):
        dp_curr = [INF] * len(opcoes[i])
        for j, val_j in enumerate(opcoes[i]):
            for k, val_k in enumerate(opcoes[i-1]):
                if val_k <= val_j and dp_prev[k] != INF:
                    nova_soma = dp_prev[k] + val_j
                    if nova_soma < dp_curr[j]:
                        dp_curr[j] = nova_soma
        dp_prev = dp_curr
    
    resposta = min(dp_prev)
    if resposta >= INF:
        print(-1)
    else:
        print(resposta)

if __name__ == "__main__":
    main()