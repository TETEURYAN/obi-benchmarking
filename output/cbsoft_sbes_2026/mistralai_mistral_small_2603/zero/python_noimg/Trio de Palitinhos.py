
import sys

def main():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    a.sort()
    count = 0
    for i in range(n - 2):
        k = i + 2
        for j in range(i + 1, n - 1):
            while k < n and a[i] + a[j] > a[k]:
                k += 1
            count += k - j - 1
    print(count)

if __name__ == "__main__":
    main()
