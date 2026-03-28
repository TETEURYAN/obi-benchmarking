import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

h = int(input_data[0])
m = int(input_data[1])
s = int(input_data[2])
t = int(input_data[3])

total_seconds = h * 3600 + m * 60 + s + t

new_s = total_seconds % 60
total_seconds //= 60
new_m = total_seconds % 60
total_seconds //= 60
new_h = total_seconds % 24

print(new_h)
print(new_m)
print(new_s)