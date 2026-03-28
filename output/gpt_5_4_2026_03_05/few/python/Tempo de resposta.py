import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

n = int(data[0])
idx = 1

current_time = 0
pending = {}
total = {}
friends = set()

for _ in range(n):
    typ = data[idx]
    x = int(data[idx + 1])
    idx += 2

    if typ == 'T':
        current_time += x
    elif typ == 'R':
        friends.add(x)
        if x not in total:
            total[x] = 0
        pending[x] = current_time
        current_time += 1
    else:  # 'E'
        friends.add(x)
        if x not in total:
            total[x] = 0
        if x in pending:
            total[x] += current_time - pending[x]
            del pending[x]
        current_time += 1

for x in pending:
    total[x] = -1

out = []
for x in sorted(friends):
    out.append(f"{x} {total[x]}")
sys.stdout.write("\n".join(out))