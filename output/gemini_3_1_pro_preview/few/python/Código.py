import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
seq = input_data[1:]

count = 0
for i in range(n - 2):
    if seq[i] == '1' and seq[i+1] == '0' and seq[i+2] == '0':
        count += 1

print(count)