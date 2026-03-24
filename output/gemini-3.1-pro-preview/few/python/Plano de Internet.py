import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

x = int(input_data[0])
n = int(input_data[1])

total_quota = x * (n + 1)
used_quota = sum(int(m) for m in input_data[2:2+n])

print(total_quota - used_quota)