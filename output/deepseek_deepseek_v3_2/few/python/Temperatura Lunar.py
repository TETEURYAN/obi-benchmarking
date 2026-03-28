import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    test_num = 1
    out_lines = []
    while True:
        N = int(data[idx])
        M = int(data[idx + 1])
        idx += 2
        if N == 0 and M == 0:
            break
        temps = list(map(int, data[idx:idx + N]))
        idx += N

        # prefix sum
        prefix = [0] * (N + 1)
        for i in range(N):
            prefix[i + 1] = prefix[i] + temps[i]

        min_avg = 10**9
        max_avg = -10**9
        for i in range(N - M + 1):
            s = prefix[i + M] - prefix[i]
            avg = s // M  # truncamento da média
            if avg < min_avg:
                min_avg = avg
            if avg > max_avg:
                max_avg = avg

        out_lines.append(f"Teste {test_num}")
        out_lines.append(f"{min_avg} {max_avg}")
        out_lines.append("")
        test_num += 1

    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()