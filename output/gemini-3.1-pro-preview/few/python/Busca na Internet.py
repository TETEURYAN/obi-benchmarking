import sys

input_data = sys.stdin.read().split()
if input_data:
    t = int(input_data[0])
    print(t * 4)