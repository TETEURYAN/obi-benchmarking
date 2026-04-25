
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    N = int(data[0])
    K = int(data[1])
    T = int(data[2])

    P = list(map(int, data[3:3+N]))
    G = list(map(int, data[3+N:3+2*N]))

    positions = [i for i in range(N) if G[i] == 1]

    if K == 0:
        print(0)
        return

    positions.sort()

    def calculate_total(positions):
        total = 0
        for pos in positions:
            total += P[pos]
        return total

    current_total = calculate_total(positions)
    max_total = current_total

    for i in range(K):
        pos = positions[i]
        left = pos - 1
        right = pos + 1

        if left >= 0 and (i == 0 or left > positions[i-1]):
            new_positions = positions.copy()
            new_positions[i] = left
            new_positions.sort()
            new_total = calculate_total(new_positions)
            if new_total > max_total:
                max_total = new_total

        if right < N and (i == K-1 or right < positions[i+1]):
            new_positions = positions.copy()
            new_positions[i] = right
            new_positions.sort()
            new_total = calculate_total(new_positions)
            if new_total > max_total:
                max_total = new_total

    if T == 0:
        print(max_total)
        return

    if K == 1:
        max_total = max(max_total, max(P))
        print(max_total)
        return

    if T >= K:
        max_total = sum(sorted(P, reverse=True)[:K])
        print(max_total)
        return

    for i in range(K):
        for j in range(i+1, K):
            if j - i > T:
                continue
            new_positions = positions.copy()
            new_positions[i], new_positions[j] = new_positions[j], new_positions[i]
            new_positions.sort()
            new_total = calculate_total(new_positions)
            if new_total > max_total:
                max_total = new_total

    print(max_total)

if __name__ == "__main__":
    main()
