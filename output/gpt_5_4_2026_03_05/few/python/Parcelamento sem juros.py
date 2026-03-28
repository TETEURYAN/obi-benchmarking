import sys

data = sys.stdin.read().split()
if not data:
    exit()

V = int(data[0])
P = int(data[1])

q, r = divmod(V, P)

out = []
for i in range(P):
    if i < r:
        out.append(str(q + 1))
    else:
        out.append(str(q))

sys.stdout.write("\n".join(out))