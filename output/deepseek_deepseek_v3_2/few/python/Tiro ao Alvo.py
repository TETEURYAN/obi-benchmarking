import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    C = int(next(it))
    T = int(next(it))
    
    radii = [int(next(it)) for _ in range(C)]
    
    total = 0
    for _ in range(T):
        x = int(next(it))
        y = int(next(it))
        dist_sq = x * x + y * y
        # Busca binária para encontrar quantos círculos contêm o ponto
        lo, hi = 0, C
        while lo < hi:
            mid = (lo + hi) // 2
            if radii[mid] * radii[mid] >= dist_sq:
                hi = mid
            else:
                lo = mid + 1
        total += lo
    
    print(total)

if __name__ == "__main__":
    main()