import sys

def can_partition(values, target):
    if target < 0:
        return False
    dp = [False] * (target + 1)
    dp[0] = True
    for v in values:
        for s in range(target, v - 1, -1):
            if dp[s - v]:
                dp[s] = True
    return dp[target]

def main():
    data = sys.stdin.read().strip().split()
    idx = 0
    test_num = 1
    results = []
    while idx < len(data):
        X = int(data[idx]); Y = int(data[idx+1]); N = int(data[idx+2])
        idx += 3
        if X == 0 and Y == 0 and N == 0:
            break
        values = []
        for _ in range(N):
            values.append(int(data[idx]))
            idx += 1
        total_arca = sum(values)
        total = X + Y + total_arca
        if total % 2 != 0:
            results.append((test_num, 'N'))
        else:
            target = total // 2 - X
            if target < 0:
                results.append((test_num, 'N'))
            else:
                possible = can_partition(values, target)
                results.append((test_num, 'S' if possible else 'N'))
        test_num += 1
    out_lines = []
    for n, res in results:
        out_lines.append(f"Teste {n}")
        out_lines.append(res)
        out_lines.append("")
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()