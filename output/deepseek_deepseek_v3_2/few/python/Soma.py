import sys
from collections import defaultdict

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    K = int(next(it))
    arr = [int(next(it)) for _ in range(N)]

    prefix_sum = 0
    freq = defaultdict(int)
    freq[0] = 1
    ans = 0

    for x in arr:
        prefix_sum += x
        target = prefix_sum - K
        ans += freq.get(target, 0)
        freq[prefix_sum] += 1

    print(ans)

if __name__ == "__main__":
    main()