import sys
from math import gcd

def lcm(a, b):
    return a // gcd(a, b) * b

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    E = int(next(it))

    pos = []
    for _ in range(E):
        v = int(next(it)) - 1
        d = int(next(it))
        pos.append(v)

    pos.sort()

    if E == 1:
        print(N)
        return

    gaps = []
    for i in range(E):
        a = pos[i]
        b = pos[(i + 1) % E]
        gaps.append((b - a) % N)

    ans = 1
    for g in gaps:
        ans = lcm(ans, N // gcd(N, g))
    print(ans)

if __name__ == "__main__":
    main()
