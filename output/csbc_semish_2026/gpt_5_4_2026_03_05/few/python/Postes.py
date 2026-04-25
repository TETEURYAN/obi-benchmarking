import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n = data[0]
replace_count = 0
repair_count = 0

for x in data[1:1 + n]:
    if x < 50:
        replace_count += 1
    elif x < 85:
        repair_count += 1

print(replace_count, repair_count)