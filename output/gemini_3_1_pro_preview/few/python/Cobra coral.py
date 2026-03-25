import sys

input_data = sys.stdin.read().split()
if input_data:
    a, b, c, d = input_data[:4]
    if a == c or b == d:
        print("V")
    else:
        print("F")