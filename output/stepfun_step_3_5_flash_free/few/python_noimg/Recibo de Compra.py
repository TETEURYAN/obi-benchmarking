import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    R = int(data[0])
    K = int(data[1])
    
    dp = [[0] * (R+1) for _ in range(K+1)]
    dp[0][0] = 1
    
    for x in range(1, R+1):
        for i in range(K, 0, -1):
            for j in range(R, x-1, -1):
                dp[i][j] += dp[i-1][j-x]
    
    print(dp[K][R])

if __name__ == "__main__":
    main()