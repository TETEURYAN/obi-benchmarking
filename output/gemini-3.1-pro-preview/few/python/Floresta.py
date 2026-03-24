import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
target = 2 * n - 1
count = 0

a = 3
while a * a <= target:
    if target % a == 0:
        count += 1
    a += 2

print(count)