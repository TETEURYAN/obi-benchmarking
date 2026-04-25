import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    L = int(next(it))
    R = int(next(it))
    a = [int(next(it)) for _ in range(N)]
    a.sort()

    # Pontos candidatos para Maximin escolher são L, R e os pontos médios entre a[i] e a[i+1]
    candidates = [L, R]
    for i in range(N - 1):
        mid = (a[i] + a[i + 1]) // 2
        if L <= mid <= R:
            candidates.append(mid)
        # Também considerar mid+1 se a soma for ímpar
        if (a[i] + a[i + 1]) % 2 == 1:
            mid2 = mid + 1
            if L <= mid2 <= R:
                candidates.append(mid2)

    # Remover duplicatas e ordenar
    candidates = sorted(set(candidates))

    best_score = -10**18
    # Para cada candidato, calcular a menor diferença para qualquer a[i]
    # Usamos busca binária para eficiência
    for x in candidates:
        # Encontrar o a[i] mais próximo de x
        lo, hi = 0, N - 1
        while hi - lo > 1:
            mid = (lo + hi) // 2
            if a[mid] < x:
                lo = mid
            else:
                hi = mid
        min_diff = min(abs(x - a[lo]), abs(x - a[hi]))
        if lo > 0:
            min_diff = min(min_diff, abs(x - a[lo - 1]))
        if hi < N - 1:
            min_diff = min(min_diff, abs(x - a[hi + 1]))
        best_score = max(best_score, min_diff)

    print(best_score)

if __name__ == "__main__":
    solve()