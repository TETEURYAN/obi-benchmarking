import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
pos = [0] * (n + 1)

for i in range(n):
    athlete = int(input_data[i + 1])
    pos[athlete] = i + 1

sys.stdout.write('\n'.join(map(str, pos[1:])) + '\n')