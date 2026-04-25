import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

idx = 0
teste = 1
out = []

while True:
    P = int(data[idx])
    S = int(data[idx + 1])
    idx += 2

    if P == 0 and S == 0:
        break

    intervals = []
    for _ in range(S):
        u = int(data[idx])
        v = int(data[idx + 1])
        idx += 2
        intervals.append((u, v))

    intervals.sort()

    merged = []
    for u, v in intervals:
        if not merged or u > merged[-1][1]:
            merged.append([u, v])
        else:
            if v > merged[-1][1]:
                merged[-1][1] = v

    out.append(f"Teste {teste}")
    for u, v in merged:
        out.append(f"{u} {v}")
    out.append("")
    teste += 1

sys.stdout.write("\n".join(out))