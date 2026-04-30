
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
        b = sizes[n - k + i]
        c = sizes[n - k + i + 1]
        balance = (b - a)**2
        total_balance += balance

    print(total_balance)

if __name__ == "__main__":
    main()
