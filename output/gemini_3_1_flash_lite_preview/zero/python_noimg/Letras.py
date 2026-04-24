import sys

def solve():
    s = sys.stdin.readline().strip()
    if not s:
        print(0)
        return
    
    dp = [0] * 26
    
    for char in s:
        idx = ord(char) - ord('A')
        max_prev = 0
        for i in range(idx + 1):
            if dp[i] > max_prev:
                max_prev = dp[i]
        dp[idx] = max_prev + 1
        
    print(max(dp))

if __name__ == '__main__':
    solve()