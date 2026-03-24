import sys

input_data = sys.stdin.read().split()
if input_data:
    x = int(input_data[0])
    y = int(input_data[1])
    if 0 <= x <= 432 and 0 <= y <= 468:
        print("dentro")
    else:
        print("fora")