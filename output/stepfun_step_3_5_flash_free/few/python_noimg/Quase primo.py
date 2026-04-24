import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    N = int(data[0])
    K = int(data[1])
    primes = list(map(int, data[2:2+K]))
    primes.sort()
    
    def dfs(i, prod, sign):
        total = 0
        for j in range(i, K):
            p = primes[j]
            if prod > N // p:
                break
            new_prod = prod * p
            total += sign * (N // new_prod)
            total += dfs(j+1, new_prod, -sign)
        return total
    
    ans = N - dfs(0, 1, 1)
    print(ans)

if __name__ == "__main__":
    main()