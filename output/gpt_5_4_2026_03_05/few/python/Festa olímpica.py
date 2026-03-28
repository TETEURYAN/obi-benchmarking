import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

N = data[0]
M = data[1]
T = data[2:2 + M]

LIMIT = 10000

lengths = [N]
for t in T:
    cur = lengths[-1]
    lengths.append(cur - cur // t)

final_len = lengths[-1]
need = min(LIMIT, final_len)

if need <= 0:
    sys.exit()

survivors = list(range(1, need + 1))

for i in range(M - 1, -1, -1):
    t = T[i]
    prev_len = lengths[i]
    new_survivors = []
    append = new_survivors.append
    for y in survivors:
        x = y + (y - 1) // (t - 1)
        if x > prev_len:
            break
        append(x)
    survivors = new_survivors
    if not survivors:
        break

sys.stdout.write("\n".join(map(str, survivors)))