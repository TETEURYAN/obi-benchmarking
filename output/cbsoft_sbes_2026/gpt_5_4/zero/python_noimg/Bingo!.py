import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(data)

    N = next(it)
    K = next(it)
    U = next(it)

    appears_in = [[] for _ in range(U + 1)]
    remaining = [K] * N

    for card in range(N):
        for _ in range(K):
            x = next(it)
            appears_in[x].append(card)

    draw_order = [next(it) for _ in range(U)]

    winners = []
    for x in draw_order:
        for card in appears_in[x]:
            remaining[card] -= 1
            if remaining[card] == 0:
                winners.append(card + 1)
        if winners:
            winners.sort()
            print(*winners)
            return

if __name__ == "__main__":
    main()
