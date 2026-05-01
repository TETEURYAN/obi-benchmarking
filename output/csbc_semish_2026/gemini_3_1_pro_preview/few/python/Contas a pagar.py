import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

v = int(input_data[0])
bills = [int(input_data[1]), int(input_data[2]), int(input_data[3])]

bills.sort()

count = 0
for bill in bills:
    if v >= bill:
        v -= bill
        count += 1
    else:
        break

print(count)