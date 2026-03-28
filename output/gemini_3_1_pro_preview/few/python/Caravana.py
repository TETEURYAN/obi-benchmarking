import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
weights = [int(x) for x in input_data[1:n+1]]

avg = sum(weights) // n

for w in weights:
    print(avg - w)