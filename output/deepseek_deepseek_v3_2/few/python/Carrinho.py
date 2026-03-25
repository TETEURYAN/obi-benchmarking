import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    D = float(next(it))
    batteries = []
    for _ in range(N):
        P = float(next(it))
        C = float(next(it))
        batteries.append((P, C))
    
    # dp[i] = tempo mínimo para chegar na bateria i
    INF = 1e18
    dp = [INF] * N
    dp[0] = 0.0  # começa na primeira bateria (posição 0)
    
    for i in range(N):
        if dp[i] >= INF:
            continue
        Pi, Ci = batteries[i]
        for j in range(i + 1, N):
            Pj, Cj = batteries[j]
            dist = Pj - Pi
            if dist > Ci:  # não consegue alcançar com a bateria atual
                break
            # velocidade ótima para ir de i para j: minimiza tempo dado que dist = Ci / V
            # tempo = dist / V, mas V = Ci / dist (pois dist = Ci / V => V = Ci / dist)
            # Na verdade, a relação é: dmax = Ci / V, e queremos dmax >= dist.
            # Para minimizar tempo, queremos a maior V possível que satisfaça dmax >= dist.
            # Isso ocorre quando dmax = dist, ou seja, V = Ci / dist.
            V = Ci / dist
            time = dist / V  # que é dist / (Ci / dist) = dist * dist / Ci
            dp[j] = min(dp[j], dp[i] + time)
    
    # Agora considerar chegar ao final D a partir de cada bateria
    ans = INF
    for i in range(N):
        if dp[i] >= INF:
            continue
        Pi, Ci = batteries[i]
        dist = D - Pi
        if dist <= Ci:  # consegue chegar ao final
            V = Ci / dist
            time = dist / V  # = dist * dist / Ci
            ans = min(ans, dp[i] + time)
    
    print(f"{ans:.3f}")

if __name__ == "__main__":
    main()