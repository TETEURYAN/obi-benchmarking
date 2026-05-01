import sys

data = sys.stdin.read().split('\n')
idx = 0
n = int(data[idx]); idx += 1

best_name = None
best_val = -1

for _ in range(n):
    name = data[idx].strip(); idx += 1
    val = int(data[idx].strip()); idx += 1
    if val > best_val:
        best_val = val
        best_name = name

if best_name is not None:
    print(best_name)
    print(best_val)