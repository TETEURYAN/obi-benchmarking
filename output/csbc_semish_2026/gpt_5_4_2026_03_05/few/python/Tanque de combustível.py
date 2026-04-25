import sys

data = sys.stdin.read().split()
if not data:
    exit()

C = int(data[0])
D = int(data[1])
T = int(data[2])

need = D / C
buy = need - T
if buy < 0:
    buy = 0.0

print(f"{buy:.1f}")