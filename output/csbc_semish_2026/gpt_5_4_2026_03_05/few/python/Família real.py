import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n, m = data[0], data[1]
parents = [0] + data[2:2 + n]
present_list = data[2 + n:2 + n + m]

depth = [0] * (n + 1)
gen_total = []
gen_present = []

for i in range(1, n + 1):
    d = depth[parents[i]] + 1
    depth[i] = d
    if d > len(gen_total):
        gen_total.append(0)
        gen_present.append(0)
    gen_total[d - 1] += 1

for x in present_list:
    d = depth[x]
    gen_present[d - 1] += 1

ans = []
for i in range(len(gen_total)):
    pct = gen_present[i] * 100.0 / gen_total[i]
    ans.append(f"{pct:.2f}")

print(" ".join(ans))