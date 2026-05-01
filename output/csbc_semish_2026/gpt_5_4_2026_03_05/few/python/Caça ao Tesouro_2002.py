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

    values = data[idx:idx + n]
    idx += n

    total_chest = sum(values)
    diff = y - x
    target_num = total_chest + diff

    possible = False
    if target_num % 2 == 0:
        target = target_num // 2
        if 0 <= target <= total_chest:
            dp = 1
            for v in values:
                dp |= dp << v
            possible = ((dp >> target) & 1) != 0

    out.append(f"Teste {teste}")
    out.append("S" if possible else "N")
    out.append("")
    teste += 1

sys.stdout.write("\n".join(out))