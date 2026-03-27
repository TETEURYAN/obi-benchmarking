
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    k = int(data[1])
    sizes = list(map(int, data[2:2+n]))
    sizes.sort()

    total_balance = 0
    left = 0
    right = n - 1

    for _ in range(k):
        a = sizes[left]
        b = sizes[left + 1]
        c = sizes[right]
        balance1 = (b - a) ** 2

        a2 = sizes[left]
        b2 = sizes[right - 1]
        c2 = sizes[right]
        balance2 = (b2 - a2) ** 2

        if balance1 <= balance2:
            total_balance += balance1
            left += 2
        else:
            total_balance += balance2
            right -= 2

    print(total_balance)

if __name__ == "__main__":
    main()
