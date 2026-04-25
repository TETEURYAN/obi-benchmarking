import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    C = int(data[0])
    tiles = list(map(int, data[1:1+C]))
    
    # DP: dp[i] = min pulos para chegar na lajota i (0-indexed)
    INF = 10**9
    dp = [INF] * C
    dp[0] = 0
    
    for i in range(C):
        if dp[i] == INF or tiles[i] == 0:
            continue
        # Pode pular para i+1 ou i+2
        for jump in range(1, 3):
            nxt = i + jump
            if nxt < C and tiles[nxt] == 1:
                dp[nxt] = min(dp[nxt], dp[i] + 1)
    
    result = dp[C-1]
    print(-1 if result == INF else result)

if __name__ == "__main__":
    main()