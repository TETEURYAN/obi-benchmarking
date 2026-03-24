import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
s = int(input_data[1])

freq = [0] * 1000005
freq[0] = 1

current_sum = 0
count = 0

for i in range(2, n + 2):
    current_sum += int(input_data[i])
    if current_sum >= s:
        count += freq[current_sum - s]
    freq[current_sum] += 1

print(count)