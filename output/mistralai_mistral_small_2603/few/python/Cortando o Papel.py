
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    heights = list(map(int, data[1:n+1]))

    max_height = max(heights)
    min_height = min(heights)

    if max_height == min_height:
        print(1)
        return

    freq = {}
    for h in heights:
        freq[h] = freq.get(h, 0) + 1

    sorted_heights = sorted(freq.keys())
    max_pieces = 0

    for i in range(len(sorted_heights) - 1):
        current = sorted_heights[i]
        next_h = sorted_heights[i + 1]
        pieces = 0
        for h in sorted_heights:
            if h <= current:
                pieces += freq[h]
        max_pieces = max(max_pieces, pieces)

    print(max_pieces)

if __name__ == "__main__":
    main()
