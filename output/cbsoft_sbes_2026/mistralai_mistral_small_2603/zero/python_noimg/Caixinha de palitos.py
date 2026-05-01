
def main():
    import sys
    N, M = map(int, sys.stdin.readline().split())
    if M * 3 < N:
        print(0)
        return
    total = 0
    max_r = min(M, N - 2)
    for r in range(1, max_r + 1):
        remaining = N - r
        if remaining < 2:
            break
        max_g = min(M, remaining - 1)
        if max_g < 1:
            continue
        total += max_g - 1 + 1
    print(total)

if __name__ == "__main__":
    main()
