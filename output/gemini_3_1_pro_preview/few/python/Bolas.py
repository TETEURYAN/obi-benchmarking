import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

counts = {}
for x in input_data:
    counts[x] = counts.get(x, 0) + 1

if any(c > 4 for c in counts.values()):
    print("N")
else:
    print("S")