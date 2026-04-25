import sys

def main():
    data = sys.stdin.read().strip()
    if not data:
        return

    s = data

    # dp[i] = maior subsequência crescente terminando com a letra i (A=0, Z=25)
    dp = [0] * 26

    for char in s:
        idx = ord(char) - ord('A')
        # Para letra char, só podemos considerar dp[j] para j <= idx
        best_prev = 0
        for j in range(idx + 1):
            if dp[j] > best_prev:
                best_prev = dp[j]
        dp[idx] = best_prev + 1

    answer = max(dp)
    print(answer)

if __name__ == "__main__":
    main()