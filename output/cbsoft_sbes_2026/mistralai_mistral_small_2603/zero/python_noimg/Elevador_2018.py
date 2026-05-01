
def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    N = int(input[ptr])
    ptr += 1
    pesos = list(map(int, input[ptr:ptr+N]))
    ptr += N

    pesos.sort()
    total = sum(pesos)
    if total % 2 != 0:
        print('N')
        return

    half = total // 2
    dp = [False] * (half + 1)
    dp[0] = True

    for peso in pesos:
        for j in range(half, peso - 1, -1):
            if dp[j - peso]:
                dp[j] = True

    if dp[half]:
        print('S')
    else:
        print('N')

if __name__ == '__main__':
    main()
