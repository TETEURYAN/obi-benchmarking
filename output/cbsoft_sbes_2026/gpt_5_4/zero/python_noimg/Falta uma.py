import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    total = 1
    for i in range(2, n + 1):
        total *= i

    cnt = [0] * (n + 1)
    idx = 1
    for _ in range(total - 1):
        for _ in range(n):
            cnt[data[idx]] += 1
            idx += 1

    ans = []
    target = total // n
    for x in range(1, n + 1):
        if cnt[x] < target * n:
            pass

    for pos in range(n):
        expected = total // n
        for x in range(1, n + 1):
            if cnt[x] % expected != 0:
                ans.append(x)
                cnt[x] += 1
                break

    if len(ans) != n:
        # Método correto por posição
        idx = 1
        poscnt = [[0] * (n + 1) for _ in range(n)]
        for _ in range(total - 1):
            for p in range(n):
                poscnt[p][data[idx]] += 1
                idx += 1
        ans = []
        expected = total // n
        for p in range(n):
            for x in range(1, n + 1):
                if poscnt[p][x] < expected:
                    ans.append(x)
                    break

    print(*ans)

if __name__ == "__main__":
    main()