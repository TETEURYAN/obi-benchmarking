
def main():
    import sys
    N, M = map(int, sys.stdin.readline().split())
    total = 0
    max_possible = min(M, N - 3 + 1)
    if max_possible < 1:
        print(0)
        return
    for r in range(1, max_possible + 1):
        remaining_after_r = N - r
        max_g = min(M, remaining_after_r - 1)
        if max_g < 1:
            continue
        min_g = max(1, remaining_after_r - M)
        if min_g > max_g:
            continue
        total += max_g - min_g + 1
    print(total)

if __name__ == "__main__":
    main()
