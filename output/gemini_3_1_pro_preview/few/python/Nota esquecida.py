import sys

input_data = sys.stdin.read().split()
if input_data:
    a = int(input_data[0])
    m = int(input_data[1])
    print(2 * m - a)