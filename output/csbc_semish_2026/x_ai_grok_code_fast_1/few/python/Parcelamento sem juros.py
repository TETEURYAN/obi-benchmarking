import sys

input_data = sys.stdin.read().split()
V = int(input_data[0])
P = int(input_data[1])
base = V // P
resto = V % P
for i in range(P):
    if i < resto:
        print(base + 1)
    else:
        print(base)