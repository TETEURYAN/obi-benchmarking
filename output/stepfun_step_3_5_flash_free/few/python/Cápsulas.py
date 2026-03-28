import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    F = int(next(it))
    ciclos = [int(next(it)) for _ in range(N)]
    
    low, high = 0, 10**8
    while low < high:
        mid = (low + high) // 2
        total = 0
        for c in ciclos:
            total += mid // c
            if total >= F:
                break
        if total >= F:
            high = mid
        else:
            low = mid + 1
    print(low)

if __name__ == "__main__":
    main()