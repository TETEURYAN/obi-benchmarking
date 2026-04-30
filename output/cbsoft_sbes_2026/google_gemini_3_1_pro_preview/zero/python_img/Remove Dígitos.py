
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        m = 1000000
        temp = i
        while temp > 0:
            d = temp % 10
            if d > 0 and dp[i - d] < m:
                m = dp[i - d]
            temp //= 10
        dp[i] = m + 1
        
    print(dp[n])

if __name__ == '__main__':
    solve()
