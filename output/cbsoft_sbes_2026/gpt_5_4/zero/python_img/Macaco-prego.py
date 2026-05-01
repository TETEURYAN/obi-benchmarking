import sys

data = sys.stdin.read().strip().split()
i = 0
teste = 1
out = []

while i < len(data):
    n = int(data[i])
    i += 1
    if n == 0:
        break

    left = -10**9
    top = 10**9
    right = 10**9
    bottom = -10**9

    for _ in range(n):
        x = int(data[i]); y = int(data[i + 1]); u = int(data[i + 2]); v = int(data[i + 3])
        i += 4

        left = max(left, x)
        top = min(top, y)
        right = min(right, u)
        bottom = max(bottom, v)

    out.append(f"Teste {teste}")
    if left < right and top > bottom:
        out.append(f"{left} {top} {right} {bottom}")
    else:
        out.append("nenhum")
    out.append("")
    teste += 1

sys.stdout.write("\n".join(out))