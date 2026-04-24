import sys

data = list(map(int, sys.stdin.read().split()))
out = []
i = 0
teste = 1

while i + 3 < len(data):
    x1, y1, x2, y2 = data[i], data[i + 1], data[i + 2], data[i + 3]
    i += 4

    if x1 == 0 and y1 == 0 and x2 == 0 and y2 == 0:
        break

    n = data[i]
    i += 1

    cnt = 0
    for _ in range(n):
        x, y = data[i], data[i + 1]
        i += 2
        if x1 <= x <= x2 and y2 <= y <= y1:
            cnt += 1

    out.append(f"Teste {teste}")
    out.append(str(cnt))
    out.append("")
    teste += 1

sys.stdout.write("\n".join(out))