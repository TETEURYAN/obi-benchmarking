
import sys

def solve():
    s = sys.stdin.read().strip()
    if not s:
        return
    
    dp = [0] * 26
    for char in s:
        idx = ord(char) - 65
        dp[idx] = max(dp[:idx + 1]) + 1
        
    print(max(dp))

if __name__ == '__main__':
    solve()
