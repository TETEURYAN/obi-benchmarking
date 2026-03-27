
import sys
from collections import defaultdict

def main():
    data = sys.stdin.read().split()
    if not data:
        print('N')
        return

    n = int(data[0])
    arcs = list(map(int, data[1:n+1]))

    total = sum(arcs)
    if total % 2 != 0:
        print('N')
        return

    target = total // 2
    dp = defaultdict(bool)
    dp[0] = True

    for arc in arcs:
        keys = list(dp.keys())
        for k in keys:
            new_k = k + arc
            if new_k <= target:
                dp[new_k] = True
            if dp.get(target, False):
                print('S')
                return

    print('N')

if __name__ == '__main__':
    main()
