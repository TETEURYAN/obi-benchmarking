import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

n = int(data[0])

best_name = ""
best_value = -1
idx = 1

for _ in range(n):
    name = data[idx]
    value = int(data[idx + 1])
    idx += 2
    if value > best_value:
        best_value = value
        best_name = name

if n > 0:
    sys.stdout.write(best_name + "\n" + str(best_value))