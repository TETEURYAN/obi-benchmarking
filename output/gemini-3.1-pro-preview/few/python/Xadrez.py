import sys

input_data = sys.stdin.read().split()
if input_data:
    L = int(input_data[0])
    C = int(input_data[1])
    if (L + C) % 2 == 0:
        print(1)
    else:
        print(0)