import sys
import math

data = sys.stdin.read().strip().split()
it = iter(data)

out = []
teste = 1

for token in it:
    n = int(token)
    if n == 0:
        break

    pts = []
    for _ in range(n):
        x = int(next(it))
        y = int(next(it))
        pts.append((x, y))

    max_d2 = 0
    for i in range(n):
        xi, yi = pts[i]
        local_max = 0
        for j in range(n):
            xj, yj = pts[j]
            dx = xi - xj
            dy = yi - yj
            d2 = dx * dx + dy * dy
            if d2 > local_max:
                local_max = d2
        if local_max < max_d2 or i == 0:
            max_d2 = local_max

    diameter = math.ceil(math.sqrt(max_d2) + 5 - 1e-12)

    out.append(f"Teste {teste}")
    out.append(str(diameter))
    out.append("")
    teste += 1

sys.stdout.write("\n".join(out))