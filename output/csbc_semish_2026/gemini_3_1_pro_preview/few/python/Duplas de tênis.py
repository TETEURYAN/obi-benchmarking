import sys

input_data = sys.stdin.read().split()
if input_data:
    a = int(input_data[0])
    b = int(input_data[1])
    c = int(input_data[2])
    d = int(input_data[3])
    print(abs((a + d) - (b + c)))