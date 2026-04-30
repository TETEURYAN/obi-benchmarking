
import sys

def nCr2(n):
    if n < 2:
        return 0
    return n * (n - 1) // 2

def solve():
    input_data = sys.stdin.read().split()
    if len(input_data) < 2:
        return
    N = int(input_data[0])
    M = int(input_data[1])
    
    S = N - 3
    if S < 0:
        print(0)
        return
        
    ans = nCr2(S + 2)
    ans -= 3 * nCr2(S - M + 2)
    ans += 3 * nCr2(S - 2 * M + 2)
    ans -= nCr2(S - 3 * M + 2)
    
    print(ans)

if __name__ == '__main__':
    solve()
