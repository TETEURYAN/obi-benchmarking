import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
p = int(input_data[1])

days = 0
bacteria = 1

while bacteria * p <= n:
    bacteria *= p
    days += 1

print(days)