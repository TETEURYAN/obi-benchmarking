import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    it = iter(data)
    N = next(it)
    K = next(it)
    U = next(it)

    appears = [[] for _ in range(U + 1)]
    remaining = [K] * N

    for card in range(N):
        for _ in range(K):
            x = next(it)
            appears[x].append(card)

    winners = []
    for draw_index in range(1, U + 1):
        x = next(it)
        for card in appears[x]:
            remaining[card] -= 1
            if remaining[card] == 0:
                winners.append(card + 1)
        if winners:
            winners.sort()
            print(*winners)
            return

if __name__ == "__main__":
    main()
