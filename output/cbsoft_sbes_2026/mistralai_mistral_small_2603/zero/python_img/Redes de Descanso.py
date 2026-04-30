
import sys
from collections import defaultdict

def main():
    n = int(sys.stdin.readline())
    heights = list(map(int, sys.stdin.readline().split()))

    groups = defaultdict(list)
    for i, h in enumerate(heights):
        groups[h].append(i)

    count = 0
    for h in groups:
        positions = groups[h]
        if len(positions) < 2:
            continue
        positions.sort()
        taken = [False] * len(positions)
        res = 0
        for i in range(len(positions)):
            if taken[i]:
                continue
            res += 1
            taken[i] = True
            current_pos = positions[i]
            for j in range(i + 1, len(positions)):
                if not taken[j] and positions[j] > current_pos:
                    taken[j] = True
                    current_pos = positions[j]
        count += res
    print(count)

if __name__ == "__main__":
    main()
