import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

x = int(data[0])
out = []

for s in data[1:]:
    t = int(s)
    if t > x:
        out.append("menor")
    elif t < x:
        out.append("maior")
    else:
        out.append("correto")

sys.stdout.write("\n".join(out))