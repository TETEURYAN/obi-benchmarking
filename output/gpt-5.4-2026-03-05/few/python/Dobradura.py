import sys

data = sys.stdin.read().split()
out = []
t = 1

for s in data:
    n = int(s)
    if n == -1:
        break
    pieces = (1 << n) + 1
    pieces *= pieces
    out.append(f"Teste {t}")
    out.append(str(pieces))
    out.append("")
    t += 1

sys.stdout.write("\n".join(out))