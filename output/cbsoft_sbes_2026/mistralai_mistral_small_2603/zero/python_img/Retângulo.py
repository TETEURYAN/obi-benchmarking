
import sys
from collections import defaultdict

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    arcs = list(map(int, data[1:n+1]))

    total = sum(arcs)
    half = total // 2

    if total % 2 != 0:
        print('N')
        return

    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i+1] = prefix[i] + arcs[i]

    freq = defaultdict(int)
    for i in range(n):
        for j in range(i+1, n):
            dist = prefix[j] - prefix[i]
            if dist == half:
                print('S')
                return
            if dist < half:
                freq[dist] += 1
            else:
                dist = total - dist
                if dist == half:
                    print('S')
                    return
                freq[dist] += 1

    if half in freq and freq[half] >= 2:
        print('S')
    else:
        print('N')

if __name__ == '__main__':
    main()
