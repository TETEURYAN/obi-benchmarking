
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    k = int(data[1])
    sizes = list(map(int, data[2:2+n]))
    sizes.sort()

    total_balance = 0
    for i in range(k):
        a = sizes[i]
        b = sizes[n - 2 - i]
        c = sizes[n - 1 - i]
        balance = (b - a) ** 2
        total_balance += balance

    print(total_balance)

if __name__ == "__main__":
    main()
