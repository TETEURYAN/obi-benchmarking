import sys

input_data = sys.stdin.read().split()

if not input_data:
    exit()

balls = list(map(int, input_data))

counts = [0] * 10
for b in balls:
    counts[b] += 1

max_freq = max(counts)

if max_freq > 4:
    print("N")
else:
    print("S")