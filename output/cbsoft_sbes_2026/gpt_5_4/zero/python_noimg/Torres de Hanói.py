import sys

nums = list(map(int, sys.stdin.read().split()))
out = []
teste = 1

for n in nums:
    if n == 0:
        break
    movimentos = (1 << n) - 1
    out.append(f"Teste {teste}")
    out.append(str(movimentos))
    out.append("")
    teste += 1

sys.stdout.write("\n".join(out))