import sys

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    N = int(data[0])
    M = int(data[1])
    
    g = gcd(N, M)
    target = N // g
    
    lo, hi = 1, M
    ans = 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if gcd(N, mid) == 1:
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1
    
    print(ans)

if __name__ == "__main__":
    main()