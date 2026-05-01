import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

n = int(data[0])
weights = list(map(int, data[1:1 + n]))

target = sum(weights) // n
res = [str(target - w) for w in weights]

sys.stdout.write("\n".join(res))