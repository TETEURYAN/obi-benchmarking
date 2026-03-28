
import sys
import math

def main():
    N = int(sys.stdin.readline())
    if N < 4:
        print(0)
        return

    total = 0
    sqrtN = int(math.isqrt(N)) + 1
    for x in range(1, sqrtN):
        if N % x == 0:
            y = N // x
            if (x >= 2 and y >= 2) and (x - 1) * (y - 1) >= 1:
                total += 1
    print(total)

if __name__ == "__main__":
    main()
