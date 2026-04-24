import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    best_price = float('inf')
    idx = 1
    for _ in range(n):
        p = float(data[idx])
        g = int(data[idx + 1])
        idx += 2
        price_per_kg = (p / g) * 1000
        if price_per_kg < best_price:
            best_price = price_per_kg
    print(f"{best_price:.2f}")

if __name__ == "__main__":
    main()