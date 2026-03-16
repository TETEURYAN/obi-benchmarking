import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

H = int(input_data[0])
M = int(input_data[1])
S = int(input_data[2])
T = int(input_data[3])

total_s = H * 3600 + M * 60 + S + T

new_S = total_s % 60
total_m = total_s // 60
new_M = total_m % 60
total_h = total_m // 60
new_H = total_h % 24

print(new_H)
print(new_M)
print(new_S)