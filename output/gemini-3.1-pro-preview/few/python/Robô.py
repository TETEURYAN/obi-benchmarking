import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
c = int(input_data[1])
s = int(input_data[2])

curr = 1
count = 1 if curr == s else 0

for i in range(c):
    cmd = int(input_data[3 + i])
    curr = (curr - 1 + cmd) % n + 1
    if curr == s:
        count += 1

print(count)