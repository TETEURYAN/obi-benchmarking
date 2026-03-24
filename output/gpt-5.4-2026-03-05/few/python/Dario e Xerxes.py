import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    exit()

n = data[0]
dario_wins = 0

idx = 1
for _ in range(n):
    d = data[idx]
    x = data[idx + 1]
    if (d - x) % 5 in (1, 2):
        dario_wins += 1
    idx += 2

if dario_wins > n // 2:
    print("dario")
else:
    print("xerxes")