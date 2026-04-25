import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    D = int(next(it))
    C = [int(next(it)) for _ in range(N)]
    total = sum(C)
    P = [0] * (N + 1)
    for i in range(1, N + 1):
        P[i] = P[i-1] + C[i-1]
    freq1 = {0: 1}
    cont1 = 0
    for j in range(1, N + 1):
        alvo = P[j] - D
        cont1 += freq1.get(alvo, 0)
        freq1[P[j]] = freq1.get(P[j], 0) + 1
    X = D - total
    cont2 = 0
    freq2 = {}
    for j in range(2, N + 1):
        p = P[j-1]
        freq2[p] = freq2.get(p, 0) + 1
        alvo = p + X
        cont2 += freq2.get(alvo, 0)
    print(cont1 + cont2)

if __name__ == "__main__":
    main()