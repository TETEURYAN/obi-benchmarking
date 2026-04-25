import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
m = int(input_data[1])

collected = set()
idx = 2
for _ in range(m):
    x = int(input_data[idx])
    collected.add(x)
    idx += 1

print(n - len(collected))