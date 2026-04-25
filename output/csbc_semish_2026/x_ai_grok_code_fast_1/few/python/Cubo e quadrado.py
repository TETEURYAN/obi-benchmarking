import sys

input_data = sys.stdin.read().split()
A = int(input_data[0])
B = int(input_data[1])

count = 0
for k in range(1, 32):
    num = k ** 6
    if A <= num <= B:
        count += 1

print(count)