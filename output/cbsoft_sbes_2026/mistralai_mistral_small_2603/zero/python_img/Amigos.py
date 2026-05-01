
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    k = int(data[1])

    top = list(map(int, data[2:2+n]))
    bottom = list(map(int, data[2+n:2+2*n]))

    top_positions = [i for i, x in enumerate(top) if x == 1]
    bottom_positions = [i for i, x in enumerate(bottom) if x == 1]

    def min_swaps(positions):
        positions_sorted = sorted(positions)
        median_pos = positions_sorted[k//2]
        total = 0
        for i in range(k):
            total += abs(positions_sorted[i] - (median_pos - (k//2) + i))
        return total

    top_swaps = min_swaps(top_positions)
    bottom_swaps = min_swaps(bottom_positions)

    print(top_swaps + bottom_swaps)

if __name__ == "__main__":
    main()
