
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    F = float(data[1])
    areas = list(map(int, data[2:2+n]))

    if n == 1:
        print("0.00")
        return

    min_tax = float('inf')
    for start in range(n):
        current = areas[start:] + areas[:start]
        total = 0
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + current[i]

        cost = 0
        for i in range(1, n):
            cost += prefix[i] * F
        if cost < min_tax:
            min_tax = cost

    print("{0:.2f}".format(min_tax))

if __name__ == "__main__":
    main()
