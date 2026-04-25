import sys
from collections import defaultdict

def main():
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    s = int(data[idx]); idx += 1
    x = [int(data[idx + i]) for i in range(n)]
    idx += n

    count = 0
    prefix_count = defaultdict(int)
    prefix_count[0] = 1
    current = 0

    for val in x:
        current += val
        count += prefix_count[current - s]
        prefix_count[current] += 1

    print(count)

main()