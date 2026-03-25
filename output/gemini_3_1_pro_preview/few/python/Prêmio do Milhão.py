import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
total = 0
for i in range(1, n + 1):
    total += int(input_data[i])
    if total >= 1000000:
        print(i)
        break