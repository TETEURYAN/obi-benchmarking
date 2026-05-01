
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    q = int(data[1])
    digits = list(map(int, data[2:2+n]))

    prefix_sum = [0] * (n + 1)
    prefix_sq = [0] * (n + 1)
    prefix_len = [0] * (n + 1)

    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i-1] + digits[i-1]
        prefix_sq[i] = prefix_sq[i-1] + digits[i-1] * digits[i-1]
        prefix_len[i] = prefix_len[i-1] + 1

    out_lines = []
    idx = 2 + n
    for _ in range(q):
        L = int(data[idx])
        R = int(data[idx+1])
        idx += 2

        length = R - L + 1
        if length == 1:
            out_lines.append("0")
            continue

        total_sum = prefix_sum[R] - prefix_sum[L-1]
        total_sq = prefix_sq[R] - prefix_sq[L-1]
        total_pairs = length * (length - 1)

        sum_contrib = total_sum * 10 * (length - 1)
        sq_contrib = total_sq * 10
        cross_contrib = 0

        for i in range(L, R + 1):
            d = digits[i-1]
            cross_contrib += d * (total_sum - d)

        potential = sum_contrib + sq_contrib + cross_contrib
        out_lines.append(str(potential))

    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()
