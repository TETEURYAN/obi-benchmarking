import sys

input_data = sys.stdin.read().split()
H = int(input_data[0])
M = int(input_data[1])
S = int(input_data[2])
T = int(input_data[3])

total_sec = H * 3600 + M * 60 + S + T

new_H = (total_sec // 3600) % 24
new_M = (total_sec // 60) % 60
new_S = total_sec % 60

print(new_H)
print(new_M)
print(new_S)