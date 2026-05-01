import sys
from bisect import bisect_left

def main():
    input = sys.stdin.readline
    C, T = map(int, input().split())
    r2 = [int(input()) ** 2 for _ in range(C)]
    total = 0

    for _ in range(T):
        x, y = map(int, input().split())
        d2 = x * x + y * y
        total += C - bisect_left(r2, d2)

    print(total)

if __name__ == "__main__":
    main()
