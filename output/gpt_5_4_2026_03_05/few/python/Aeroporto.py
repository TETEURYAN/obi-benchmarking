import sys

data = sys.stdin.read().split()
idx = 0
teste = 1
out = []

while idx + 1 < len(data):
    A = int(data[idx])
    V = int(data[idx + 1])
    idx += 2

    if A == 0 and V == 0:
        break

    deg = [0] * (A + 1)

    for _ in range(V):
        x = int(data[idx])
        y = int(data[idx + 1])
        idx += 2
        deg[x] += 1
        deg[y] += 1

    mx = max(deg[1:]) if A > 0 else 0
    ans = [str(i) for i in range(1, A + 1) if deg[i] == mx]

    out.append(f"Teste {teste}")
    out.append(" ".join(ans))
    out.append("")

    teste += 1

sys.stdout.write("\n".join(out))