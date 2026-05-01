
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
        total = 0
        i = 0
        while i < len(positions):
            if i + 1 < len(positions):
                total += 1
                i += 2
            else:
                break
        count += total
    print(count)

if __name__ == "__main__":
    main()
