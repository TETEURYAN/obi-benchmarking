import sys

data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit()

n, m = data[0], data[1]
parents = [0] + data[2:2 + n]
present_list = data[2 + n:2 + n + m]

present = [False] * (n + 1)
for x in present_list:
    present[x] = True

gen = [0] * (n + 1)
count_gen = []
present_gen = []

for i in range(1, n + 1):
    p = parents[i]
    gen[i] = gen[p] + 1
    g = gen[i]
    while len(count_gen) < g:
        count_gen.append(0)
        present_gen.append(0)
    count_gen[g - 1] += 1
    if present[i]:
        present_gen[g - 1] += 1

out = []
for c, p in zip(count_gen, present_gen):
    out.append(f"{(p * 100.0) / c:.2f}")

print(" ".join(out))