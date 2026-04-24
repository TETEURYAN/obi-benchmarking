
import sys
from itertools import combinations

def main():
    data = sys.stdin.read().split()
    R = int(data[0])
    K = int(data[1])
    count = 0
    for combo in combinations(range(1, R), K):
        if sum(combo) == R:
            count += 1
    print(count)

if __name__ == "__main__":
    main()
