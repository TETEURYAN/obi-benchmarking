
import sys

def main():
    N, K = map(int, sys.stdin.read().split())
    low = 1
    high = N
    result = 0
    while low <= high:
        mid = (low + high) // 2
        if mid * (mid + 1) // 2 >= K:
            result = mid
            high = mid - 1
        else:
            low = mid + 1
    print(result)

if __name__ == "__main__":
    main()
