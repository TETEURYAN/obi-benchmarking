import sys

def max_n_for_tests(t, k):
    """Retorna o maior N tal que com k balões e t testes conseguimos resolver."""
    total = 0
    comb = 1
    for i in range(1, k + 1):
        comb = comb * (t - i + 1) // i
        total += comb
        if total >= 10**18:
            return total
    return total

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    N = int(data[0])
    K = int(data[1])
    
    if K == 1:
        print(N)
        return
    
    low, high = 1, N
    while low < high:
        mid = (low + high) // 2
        if max_n_for_tests(mid, K) >= N:
            high = mid
        else:
            low = mid + 1
    print(low)

if __name__ == "__main__":
    solve()