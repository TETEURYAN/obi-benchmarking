import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

H = int(input_data[0])
M = int(input_data[1])
S = int(input_data[2])
T = int(input_data[3])

total_seconds = H * 3600 + M * 60 + S + T
total_seconds %= 86400

new_H = total_seconds // 3600
new_M = (total_seconds % 3600) // 60
new_S = total_seconds % 60

print(new_H)
print(new_M)
print(new_S)