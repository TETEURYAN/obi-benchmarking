
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return

    R = int(data[0])
    N = int(data[1])
    fruits = {}

    for i in range(2, 2 + N):
        t = int(data[i])
        p = int(data[i + 1])
        if t not in fruits:
            fruits[t] = p
        else:
            if p < fruits[t]:
                fruits[t] = p

    prices = sorted(fruits.values())
    count = 0
    total = 0

    for price in prices:
        if total + price <= R:
            total += price
            count += 1
        else:
            break

    print(count)

if __name__ == "__main__":
    main()
