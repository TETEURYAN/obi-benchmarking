
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    d = int(data[1])
    w = int(data[2])
    prices = list(map(int, data[3:3+n]))

    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i+1] = prefix[i] + prices[i]

    max_days = d
    left = 0
    right = n - d

    while left <= right:
        mid = (left + right) // 2
        possible = False

        for i in range(0, n - d - mid + 1):
            j = i + d + mid - 1
            if j >= n:
                break
            total = prefix[j+1] - prefix[i]
            if total <= w:
                possible = True
                break

        if possible:
            max_days = d + mid
            left = mid + 1
        else:
            right = mid - 1

    print(max_days)

if __name__ == "__main__":
    main()
