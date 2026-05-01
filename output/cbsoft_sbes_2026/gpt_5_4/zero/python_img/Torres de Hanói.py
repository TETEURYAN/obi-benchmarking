import sys

out = []
teste = 1

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    n = int(line)
    if n == 0:
        break
    movimentos = (1 << n) - 1
    out.append(f"Teste {teste}")
    out.append(str(movimentos))
    out.append("")
    teste += 1

sys.stdout.write("\n".join(out))