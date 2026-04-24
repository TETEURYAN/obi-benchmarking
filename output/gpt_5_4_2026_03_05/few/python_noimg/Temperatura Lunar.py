import sys

data = sys.stdin.read().split()
idx = 0
teste = 1
out = []

while idx + 1 < len(data):
    n = int(data[idx])
    m = int(data[idx + 1])
    idx += 2

    if n == 0 and m == 0:
        break

    temps = list(map(int, data[idx:idx + n]))
    idx += n

    window_sum = sum(temps[:m])
    min_sum = window_sum
    max_sum = window_sum

    for i in range(m, n):
        window_sum += temps[i] - temps[i - m]
        if window_sum < min_sum:
            min_sum = window_sum
        if window_sum > max_sum:
            max_sum = window_sum

    out.append(f"Teste {teste}")
    out.append(f"{min_sum // m} {max_sum // m}")
    out.append("")
    teste += 1

sys.stdout.write("\n".join(out))