import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

A = int(input_data[0])
N = int(input_data[1])

count = 0
for i in range(2, 2 + N):
    if A * int(input_data[i]) >= 40000000:
        count += 1

print(count)