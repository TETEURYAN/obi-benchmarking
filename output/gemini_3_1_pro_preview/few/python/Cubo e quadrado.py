import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

a = int(input_data[0])
b = int(input_data[1])

count = 0
x = 1
while True:
    p = x ** 6
    if p > b:
        break
    if p >= a:
        count += 1
    x += 1

print(count)