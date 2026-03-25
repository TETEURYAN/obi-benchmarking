import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    R = int(next(it))
    N = int(next(it))
    
    # Para cada tipo de fruta, guardamos o menor preço encontrado
    min_price = {}
    for _ in range(N):
        t = int(next(it))
        p = int(next(it))
        if t not in min_price or p < min_price[t]:
            min_price[t] = p
    
    # Pegamos os menores preços de cada tipo
    prices = list(min_price.values())
    prices.sort()
    
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