import sys

data = sys.stdin.read().split()
C = int(data[0])
D = int(data[1])
T = int(data[2])

needed = D / C
buy = needed - T
if buy < 0:
    buy = 0.0

print(f"{buy:.1f}")