import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    D = float(data[1])
    pos = []
    carga = []
    idx = 2
    for _ in range(n):
        p = float(data[idx])
        c = float(data[idx + 1])
        pos.append(p)
        carga.append(c)
        idx += 2
    dp = [0.0] * n
    dp[0] = 0.0
    for i in range(1, n):
        best = float('inf')
        for j in range(i):
            dist = pos[i] - pos[j]
            tempo = dp[j] + (dist * dist) / carga[j]
            if tempo < best:
                best = tempo
        dp[i] = best
    ans = float('inf')
    for j in range(n):
        dist_final = D - pos[j]
        tempo_total = dp[j] + (dist_final * dist_final) / carga[j]
        if tempo_total < ans:
            ans = tempo_total
    print(f"{ans:.3f}")

if __name__ == "__main__":
    main()