import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

n = int(data[0])
pos = [0] * (n + 1)

for i in range(1, n + 1):
    athlete = int(data[i])
    pos[athlete] = i

sys.stdout.write('\n'.join(map(str, pos[1:])))