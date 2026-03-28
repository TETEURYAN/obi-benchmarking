
import sys
from collections import defaultdict

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n, k = map(int, data[:2])
    piles = list(map(int, data[2:2+n]))

    freq = defaultdict(int)
    for p in piles:
        freq[p] += 1

    distinct = len(freq)
    if distinct <= k:
        print(0)
        return

    sorted_piles = sorted(piles)
    operations = 0

    while distinct > k:
        min_val = sorted_piles[0]
        max_val = sorted_piles[-1]

        if freq[min_val] <= freq[max_val]:
            operations += freq[min_val]
            freq[max_val] += freq[min_val]
            del freq[min_val]
            distinct -= 1
            sorted_piles = sorted(freq.keys())
        else:
            operations += freq[max_val]
            freq[min_val] += freq[max_val]
            del freq[max_val]
            distinct -= 1
            sorted_piles = sorted(freq.keys())

    print(operations)

if __name__ == "__main__":
    main()
