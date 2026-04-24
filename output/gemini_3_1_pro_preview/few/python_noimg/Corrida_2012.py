import sys

input_data = sys.stdin.read().split()
if input_data:
    c = int(input_data[0])
    n = int(input_data[1])
    print(c % n)