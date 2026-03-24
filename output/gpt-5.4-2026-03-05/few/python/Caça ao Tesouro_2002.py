import sys

data = list(map(int, sys.stdin.read().split()))
idx = 0
teste = 1
out = []

while idx + 2 < len(data):
    x = data[idx]
    y = data[idx + 1]
    n = data[idx + 2]
    idx += 3

    if x == 0 and y == 0 and n == 0:
        break

    vals = data[idx:idx + n]
    idx += n

    total = sum(vals)
    diff = y - x

    possible = False
    if (total + diff) % 2 == 0:
        target = (total + diff) // 2
        if 0 <= target <= total:
            dp = 1
            for v in vals:
                dp |= dp << v
            possible = ((dp >> target) & 1) != 0

    out.append(f"Teste {teste}")
    out.append("S" if possible else "N")
    out.append("")
    teste += 1

sys.stdout.write("\n".join(out))