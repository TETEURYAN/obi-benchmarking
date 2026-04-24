import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
reqs = [int(input_data[1]), int(input_data[2]), int(input_data[3])]

reqs.sort()

count = 0
for req in reqs:
    if n >= req:
        n -= req
        count += 1
    else:
        break

print(count)