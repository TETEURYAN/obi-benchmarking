
import sys
from collections import defaultdict

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    arcs = list(map(int, data[1:n+1]))

    total = sum(arcs)
    if total % 4 != 0:
        print('N')
        return

    target = total // 4
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i+1] = prefix[i] + arcs[i]

    freq = defaultdict(int)
    for i in range(n):
        current = prefix[i]
        for j in range(i+1, n):
            s = current + arcs[j]
            if s > target:
                break
            if s == target:
                freq[target] += 1
                break
            if (target - s) in freq:
                print('S')
                return
            freq[s] += 1

    print('N')

if __name__ == '__main__':
    main()
