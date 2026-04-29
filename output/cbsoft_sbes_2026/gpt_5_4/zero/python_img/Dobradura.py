import sys

out = []
teste = 1

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    n = int(line)
    if n == -1:
        break
    pieces = (2 ** n + 1) ** 2
    out.append(f"Teste {teste}")
    out.append(str(pieces))
    out.append("")
    teste += 1

sys.stdout.write("\n".join(out))