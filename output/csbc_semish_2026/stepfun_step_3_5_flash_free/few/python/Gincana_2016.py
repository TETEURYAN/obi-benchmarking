import sys
import math

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    N = int(data[0])
    M = int(data[1])
    start = M
    end = max(1, M - 47)
    for x in range(start, end - 1, -1):
        if math.gcd(x, N) == 1:
            print(x)
            return
    print(1)

if __name__ == "__main__":
    main()