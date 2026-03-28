import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
lives = [int(x) for x in input_data[1:n+1]]

max_so_far = 0
current_max = 0

for x in lives:
    current_max += x
    if current_max < 0:
        current_max = 0
    elif current_max > max_so_far:
        max_so_far = current_max

print(max_so_far)