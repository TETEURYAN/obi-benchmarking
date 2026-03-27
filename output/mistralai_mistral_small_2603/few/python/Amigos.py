
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    N = int(data[0])
    K = int(data[1])

    a = list(map(int, data[2:2+N]))
    b = list(map(int, data[2+N:2+2*N]))

    upper_positions = [i for i in range(N) if a[i] == 1]
    lower_positions = [i for i in range(N) if b[i] == 1]

    upper_positions.sort()
    lower_positions.sort()

    def min_swaps(positions):
        swaps = 0
        target = positions.copy()
        target.sort()
        for i in range(len(positions)):
            if positions[i] != target[i]:
                for j in range(i + 1, len(positions)):
                    if positions[j] == target[i]:
                        positions[i], positions[j] = positions[j], positions[i]
                        swaps += j - i
                        break
        return swaps

    total_swaps = 0
    total_swaps += min_swaps(upper_positions)
    total_swaps += min_swaps(lower_positions)

    print(total_swaps)

if __name__ == "__main__":
    main()
