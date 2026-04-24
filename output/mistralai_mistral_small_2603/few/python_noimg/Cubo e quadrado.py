
import sys
import math

def main():
    data = sys.stdin.read().split()
    A = int(data[0])
    B = int(data[1])

    count = 0
    max_k = int(math.isqrt(B)) + 2
    for k in range(1, max_k + 1):
        num = k ** 6
        if A <= num <= B:
            count += 1
    print(count)

if __name__ == "__main__":
    main()
