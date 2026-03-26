import sys

input_data = sys.stdin.read().split()

if not input_data:
    exit()

n = int(input_data[0])

if n == 1:
    print(1)
    exit()

seq = list(map(int, input_data[1:]))

count = 1
current_diff = seq[1] - seq[0]

for i in range(2, n):
    diff = seq[i] - seq[i-1]
    if diff != current_diff:
        count += 1
        current_diff = diff

print(count)