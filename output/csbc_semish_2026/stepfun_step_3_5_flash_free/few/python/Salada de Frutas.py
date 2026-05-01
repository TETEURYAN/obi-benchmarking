import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    R = int(data[0])
    N = int(data[1])
    idx = 2
    min_price = {}
    for _ in range(N):
        t = int(data[idx])
        p = int(data[idx + 1])
        idx += 2
        if t not in min_price or p < min_price[t]:
            min_price[t] = p
    prices = sorted(min_price.values())
    total = 0
    count = 0
    for price in prices:
        if total + price <= R:
            total += price
            count += 1
        else:
            break
    print(count)

if __name__ == "__main__":
    main()