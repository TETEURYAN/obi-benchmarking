
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    piles = list(map(int, data[1:n+1]))

    total = sum(piles)
    k = n
    min_moves = float('inf')

    for h in range(1, n + 1):
        required = k * (h + (h + k - 1)) // 2
        if required > total:
            continue
        if (total - required) % k != 0:
            continue
        moves = 0
        current = h
        for p in piles:
            if p > current:
                moves += p - current
            current += 1
        if moves < min_moves:
            min_moves = moves

    if min_moves != float('inf'):
        print(min_moves)
    else:
        print(-1)

if __name__ == "__main__":
    main()
