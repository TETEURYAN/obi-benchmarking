import sys

data = sys.stdin.read().strip().split()
i = 0
teste = 1
out = []

while i < len(data):
    s = int(data[i])
    i += 1
    if s == 0:
        break

    xs = []
    ys = []
    for _ in range(s):
        x = int(data[i])
        y = int(data[i + 1])
        i += 2
        xs.append(x)
        ys.append(y)

    xs.sort()
    ys.sort()

    mx = xs[s // 2]
    my = ys[s // 2]

    out.append(f"Teste {teste}")
    out.append(f"{mx} {my}")
    out.append("")

    teste += 1

sys.stdout.write("\n".join(out))