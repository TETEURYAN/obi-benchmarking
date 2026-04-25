
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    a = list(map(int, data[1:n+1]))

    total = sum(a)
    left_sum = 0
    for k in range(n):
        left_sum += a[k]
        if left_sum == total - left_sum:
            print(k + 1)
            return

if __name__ == "__main__":
    main()
