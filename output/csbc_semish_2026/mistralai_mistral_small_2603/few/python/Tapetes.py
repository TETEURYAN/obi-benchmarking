
import sys

def main():
    L, N = map(int, sys.stdin.read().split())
    if N == 1:
        print(L * L)
        return

    min_sum = N * (N + 1) // 2
    if L < min_sum:
        print(0)
        return

    remaining = L - min_sum
    max_area = 0
    for i in range(1, N + 1):
        current = i + remaining
        max_area += current * current

    print(max_area)

if __name__ == "__main__":
    main()
