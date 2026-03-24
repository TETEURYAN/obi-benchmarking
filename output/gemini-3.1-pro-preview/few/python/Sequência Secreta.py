import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
if n == 0:
    print(0)
    exit()

seq = input_data[1:]
count = 1
last = seq[0]

for i in range(1, n):
    if seq[i] != last:
        count += 1
        last = seq[i]

print(count)