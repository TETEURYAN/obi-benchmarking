
import sys

def C(n):
    if n < 2:
        return 0
    return n * (n - 1) // 2

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    N = int(input_data[0])
    M = int(input_data[1])
    
    ans = C(N - 1) - 3 * C(N - M - 1) + 3 * C(N - 2 * M - 1) - C(N - 3 * M - 1)
    print(ans)

if __name__ == '__main__':
    solve()
