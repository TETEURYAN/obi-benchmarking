import sys
from bisect import bisect_left

def main():
    data = sys.stdin.buffer.read().split()
    it = iter(data)

    C = int(next(it))
    T = int(next(it))

    r2 = [0] * C
    for i in range(C):
        r = int(next(it))
        r2[i] = r * r

    total = 0
    for _ in range(T):
        x = int(next(it))
        y = int(next(it))
        d2 = x * x + y * y
        total += C - bisect_left(r2, d2)

    print(total)

if __name__ == "__main__":
    main()