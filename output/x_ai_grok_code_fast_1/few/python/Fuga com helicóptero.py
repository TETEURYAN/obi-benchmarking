import sys

input_data = sys.stdin.read().split()
H = int(input_data[0])
P = int(input_data[1])
F = int(input_data[2])
D = int(input_data[3])

if D == 1:
    dist_H = (H - F) % 16
    dist_P = (P - F) % 16
else:
    dist_H = (F - H) % 16
    dist_P = (F - P) % 16

if dist_H < dist_P:
    print("S")
else:
    print("N")